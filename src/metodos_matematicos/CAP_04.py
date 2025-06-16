import time

import holoviews as hv
import numpy as np
import panel as pn
import param
from scipy import stats

pn.extension()
hv.extension('bokeh')

class DiscreteProbabilityDistribution(param.Parameterized):
    n_trials = param.Integer(default=10, bounds=(1, 100))
    p = param.Number(default=0.5, bounds=(0, 1))
    n_repetitions = param.Integer(default=1000, bounds=(10, 10000))

    distributions = param.List(default=["Binomial"], item_type=str)

    def draw_binomial(self, n_samples=None):
        if n_samples is None:
            n_samples = self.n_repetitions
        return np.random.binomial(n=self.n_trials, p=self.p, size=n_samples)

    def draw_poisson(self):
        lam = self.n_trials * self.p
        return np.random.poisson(lam=lam, size=self.n_repetitions)

    def pmf_binomial(self):
        x = np.arange(0, self.n_trials + 5)
        pmf = stats.binom.pmf(x, self.n_trials, self.p)
        return hv.Scatter((x, pmf), kdims='k').opts(color='cadetblue', marker="square", size=5)

    def pmf_poisson(self):
        lam = self.n_trials * self.p
        x = np.arange(0, int(lam + 10))
        pmf = stats.poisson.pmf(x, mu=lam)
        return hv.Scatter((x, pmf), kdims='k').opts(color='maroon', marker="square", size=5)

    def pdf_normal(self):
        mu = stats.binom.mean(self.n_trials, self.p)
        sigma = stats.binom.std(self.n_trials, self.p)
        x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 300)
        pdf = stats.norm.pdf(x, loc=mu, scale=sigma)
        return hv.Curve((x, pdf), kdims='x', vdims='pdf').opts(color='magenta', line_width=2)

    @param.depends('n_trials', 'p', 'n_repetitions', 'distributions')
    def make_frame(self):
        overlays = []

        if 'Binomial' in self.distributions:
            samples = self.draw_binomial()
            values, counts = np.unique(samples, return_counts=True)
            freqs = counts / self.n_repetitions
            hist = hv.Bars((values, freqs), kdims='k', vdims='Freq').opts(color='skyblue', alpha=0.5)
            overlays.append(hist * self.pmf_binomial())

        if 'Poisson' in self.distributions:
            samples = self.draw_poisson()
            values, counts = np.unique(samples, return_counts=True)
            freqs = counts / self.n_repetitions
            hist = hv.Bars((values, freqs), kdims='k', vdims='Freq').opts(color='salmon', alpha=0.5)
            overlays.append(hist * self.pmf_poisson())

        if 'Normal' in self.distributions:
            overlays.append(self.pdf_normal())

        if overlays:
            return hv.Overlay(overlays).opts(title="Distribuições", height=400, width=900)
        else:
            return hv.Curve([]).opts(title="Selecione ao menos uma distribuição")

    def view_distributions(self):
        checkboxes = pn.widgets.CheckBoxGroup(
            name='Distribuições',
            value=['Binomial'],
            options=['Binomial', 'Poisson', 'Normal']
        )

        def update_distributions(event):
            self.distributions = event.new

        checkboxes.param.watch(update_distributions, 'value')

        controls = pn.Param(
            self,
            parameters=['n_trials', 'p', 'n_repetitions'],
            widgets={
                'p': pn.widgets.FloatSlider,
                'n_trials': pn.widgets.IntSlider,
                'n_repetitions': pn.widgets.IntSlider,
            },
            show_name=False
        )

        dist_dmap = hv.DynamicMap(self.make_frame)

        return pn.Column(
            "# Distribuições Discretas e Contínuas",
            checkboxes,
            controls,
            dist_dmap
        )

    def view_galton_board(self):
        step = 10
        current_samples = []

        def make_frame(counter=0, **kwargs):
            if counter == 0:
                current_samples.clear()

            if len(current_samples) < self.n_repetitions:
                new_samples = self.draw_binomial(step)
                current_samples.extend(new_samples)

            values, counts = np.unique(current_samples, return_counts=True)
            freqs = counts / len(current_samples)
            hist = hv.Bars((values, freqs), kdims='k', vdims='Freq').opts(color='skyblue', alpha=0.7)
            overlay = hist * self.pmf_binomial() * self.pdf_normal()
            return overlay.opts(title=f"Galton Board - {len(current_samples)} lançamentos")

        counter_stream = hv.streams.Stream.define('Counter', counter=0)()
        dmap = hv.DynamicMap(make_frame, streams=[counter_stream])

        play_button = pn.widgets.Toggle(name='▶️ Play / ⏸ Pause', button_type='primary')

        def run_animation():
            counter_stream.event(counter=0)
            i = 0
            while play_button.value and i * step < self.n_repetitions:
                i += 1
                counter_stream.event(counter=i)
                time.sleep(0.1)

        play_button.param.watch(lambda e: pn.state.execute(run_animation) if e.new else None, 'value')

        controls = pn.Param(
            self,
            parameters=['n_trials', 'p', 'n_repetitions'],
            widgets={
                'p': pn.widgets.FloatSlider,
                'n_trials': pn.widgets.IntSlider,
                'n_repetitions': pn.widgets.IntSlider,
            },
            show_name=False
        )

        return pn.Column(
            "## Simulação: Tabuleiro de Galton (Binomial → Normal)",
            controls,
            play_button,
            dmap.opts(framewise=True, height=400, width=900)
        )


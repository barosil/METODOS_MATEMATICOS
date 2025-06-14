import holoviews as hv
import pandas as pd
import panel as pn

hv.extension('bokeh')
pn.extension()

def make_timeline(df, **kwargs):
    
    start_year = df["START"].min() - 10
    end_year = df["END"].max() + 10
    ticks = list(range((int(start_year // 10)) * 10, (int(end_year // 10 + 1)) * 10, 10))
    width = (end_year - start_year) / 30
    height = kwargs.get("height", 2)
    n_rows = kwargs.get("n_rows", 4)
    h_offset = kwargs.get("h_offset", 0.1)
    v_offset = kwargs.get("v_offset", 1)

    def make_label(start_year, start_y, height, h_offset, v_offset, n_rows, direction="up", color="marrom", text="Sociedade"):
        if direction == "up":
            start_y = start_y 
            end_y = start_y + n_rows * height
            pos_text = start_y + v_offset
        else:
            start_y = start_y 
            end_y = start_y - n_rows * height
            pos_text = end_y + v_offset
            #h_offset = -h_offset
        ylabels = hv.Rectangles((start_year - width, start_y, start_year, end_y)).opts(color=color, alpha=0.5)
        annotation = hv.Text(start_year - width/2, pos_text, text).opts(angle=90, text_align='center', text_baseline='center')
        return ylabels * annotation

    SOC_label = make_label(start_year, 1, height, h_offset, v_offset, n_rows, direction="up", color="orange", text="Sociedade")
    MAT_label = make_label(start_year, -1, height, h_offset, v_offset, n_rows, direction="down", color="maroon", text="Matemática")
    PHYS_label = make_label(start_year, -1 - (n_rows * height), height, h_offset, v_offset, n_rows, direction="down", color="cadetblue", text="Física")


    # Timeline base
    timeline = hv.HLine(0).opts(color='maroon', line_width=10, alpha=0.5)
    tick_marks = hv.Segments([(tick, 0, tick, .5) for tick in ticks]).opts(
        color='gray', line_width=2)
    tick_labels = [hv.Text(t, .8, str(t)).opts(text_align='center', text_font_size='7pt') for t in ticks]

    

    def stack_bars(df, base_y, color, direction="down", categoria=None):
        df = df[df["CATEGORIA"]==categoria].sort_values(by="START")
        df["DURACAO"] = df["END"] - df["START"]
        overlays = hv.Overlay([])
        slot_height = height
        max_slots = 4
        if direction == "down":
            _direction = -1
            _arrow_direction = "v"
        else:
            _direction = 1
            _arrow_direction = "^"
        slots = [base_y + i * _direction * slot_height for i in range(max_slots)]
        last_end = -float('inf')
        slot_index = 0

        for _, row in df.iterrows():
            if row["START"] > last_end:
                slot_index = 0  # reseta altura após intervalo

            y0 = slots[slot_index]
            y1 = y0 + 0.8
            arrow = hv.Segments([(row["START"], 0, row["START"], y0)]).opts(color=color, line_width=1)
            if row["DURACAO"] < width/30:
                df_point = pd.DataFrame({
                    "x": [row["START"]],
                    "y": [y0 + 0.2],
                    "DESCRICAO": [row["DESCRICAO"]]
                })
                shape = hv.Points(df_point, kdims=["x", "y"], vdims=["DESCRICAO"]).opts(
                    marker="square", size=8, color=color, tools=["hover"]
                )
            else:
                df_bar = pd.DataFrame({
                    "x0": [row["START"]],
                    "y0": [y0],
                    "x1": [row["END"]],
                    "y1": [y1],
                    "DESCRICAO": [row["DESCRICAO"]]
                })
                shape = hv.Rectangles(df_bar, kdims=["x0", "y0", "x1", "y1"], vdims=["DESCRICAO"]).opts(
                    color=color, tools=["hover"]
                )

            overlays *= shape * arrow
            
            
            
            last_end = row["END"]
            slot_index = (slot_index + 1) % max_slots  # avança para próximo slot
        

        return overlays


    SOC_overlay = stack_bars(df, 1., "orange", direction="up", categoria="SOCIEDADE")
    MAT_overlay = stack_bars(df, -1., "maroon", direction="down", categoria="MATEMÁTICA")
    PHYS_overlay = stack_bars(df, -1 - (n_rows * height), "cadetblue", direction="down", categoria="FÍSICA")

    final_plot = (
        timeline * tick_marks * SOC_label * MAT_label * PHYS_label *
        SOC_overlay * MAT_overlay * PHYS_overlay *
        hv.Overlay(tick_labels)
    ).opts(
        title="Linha do Tempo",
        height = 600, width=1000, yaxis=None, xaxis=None, xlim = (start_year-20, end_year)
    )

    return final_plot

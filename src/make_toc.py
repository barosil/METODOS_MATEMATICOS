from pathlib import Path

import typer


def make_toc_file(root: str = "index.md", base_dir: str = "../content"):
    """
    Gera um arquivo _toc.yml para JupyterBook a partir de arquivos .md e .ipynb em um diretório base.

    Args:
        root (str): Nome do arquivo raiz (default: "index.md")
        base_dir (str): Diretório base onde procurar os arquivos (default: "../content")
    """
    base_path = Path(base_dir).resolve()
    root_stem = Path(root).with_suffix('').as_posix()

    # Verifica se o diretório base existe
    if not base_path.exists():
        typer.echo(f"❌ Erro: Diretório '{base_path}' não encontrado.", err=True)
        raise typer.Exit(1)

    entries = [
        "format: jb-book\n",
        f"root: {root_stem}\n",
        "chapters:\n"
    ]

    try:
        files = sorted([
            file.relative_to(base_path)
            for file in base_path.rglob("*")
            if file.suffix in (".md", ".ipynb")
            and file.name != root
            and "QUADROS" not in str(file)
        ])
    except Exception as e:
        typer.echo(f"❌ Erro ao processar arquivos: {e}", err=True)
        raise typer.Exit(1)

    previous_indent = 0

    for file in files:
        file_no_suffix = file.with_suffix('').as_posix()
        parts = file.parts
        indent = len(parts) - 1

        # Adiciona seção se for mais profundo que anterior
        if indent > previous_indent and previous_indent > 0:
            entries.append(f"{'  ' * (indent-1)}  sections:\n")

        entries.append(f"{'  ' * indent}- file: {file_no_suffix}\n")
        previous_indent = indent

    filename = base_path / "_toc.yml"

    if filename.exists():
        typer.echo(f"⚠️ Aviso: Arquivo '{filename}' já existe e será sobrescrito.", err=True)

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.writelines(entries)
        typer.echo(f"✅ Arquivo '{filename}' gerado com sucesso!")
    except Exception as e:
        typer.echo(f"❌ Erro ao escrever arquivo: {e}", err=True)
        raise typer.Exit(1)

def main(root: str = "index.md", base_dir: str = "../content"):
    """
    Função principal para criar o arquivo de tabela de conteúdos (TOC) do livro.

    Args:
        root: Nome do arquivo raiz do livro.
        caminho: Caminho para o diretório onde os arquivos markdown estão localizados.
    """
    base_dir = Path(base_dir)
    if not base_dir.exists():
        typer.echo(f"Diretório {base_dir} não encontrado.")
        raise typer.Exit(code=1)
    
    make_toc_file(root, base_dir)
    

if __name__ == "__main__":
    typer.run(main)
from pathlib import Path

import typer
import yaml


def criar_estrutura(livro: list, base_dir: str = "."):
    """
    Cria uma estrutura de diretórios e arquivos markdown a partir de uma lista de capítulos (YAML carregado).
    
    Args:
        livro: Lista contendo os capítulos e seções.
        base_dir: Diretório base onde a estrutura será criada.
    """
    
    def criar_stub(caminho_arquivo: str, titulo: str, nivel: int):
        """Cria um arquivo markdown stub com um título no nível adequado."""
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(f"{'#' * nivel} {titulo}\n\n")
            f.write("*este é um stub*\n")
    
    def processar_nivel(nivel: int, itens: list, prefixo: str = "CAP", caminho_atual: str = base_dir):
        
        for i, item in enumerate(itens, start=1):
            if isinstance(item, dict):
                for titulo, subitens in item.items():
                    id_pasta = f"{prefixo}_{i:02}"
                    caminho_pasta = Path(caminho_atual) / id_pasta
                    Path(caminho_pasta).mkdir(exist_ok=True)
                    quadro_cap = Path(caminho_pasta) / f"{caminho_pasta.name}_QUADROS"
                    Path(quadro_cap).mkdir(exist_ok=True)
                    caminho_md = Path(caminho_pasta) / f"{id_pasta}.md"
                    criar_stub(caminho_md, titulo, nivel)

                    if subitens:  # Se houver subseções
                        processar_nivel(nivel + 1, subitens, prefixo=f"SEC_{i:02}", caminho_atual=caminho_pasta)
            else:
                # Caso seja apenas uma string (seção sem subseções)
                id_pasta = f"{prefixo}_{i:02}"
                caminho_pasta = Path(caminho_atual) / id_pasta
                Path(caminho_pasta).mkdir(exist_ok=True)

                caminho_md = Path(caminho_pasta) / f"{id_pasta}.md"
                criar_stub(caminho_md, item, nivel)
    
    processar_nivel(1, livro)


def main(structure_file: str="../data/structure.yaml", root: str="livro", base_dir:str="./content"):
    """
    Função principal para criar a estrutura do livro.
    
    Args:
        root: Nome do diretório raiz do livro.
        base_dir: Diretório base onde a estrutura será criada.
    """
    Path(base_dir).mkdir(exist_ok=True)
    estrutura = yaml.safe_load(open(structure_file))
    criar_estrutura(estrutura[root], base_dir=base_dir)

if __name__ == "__main__":
    typer.run(main)
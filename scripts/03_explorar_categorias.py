import pandas as pd
from pathlib import Path

# Caminhos do projeto
caminho_csv = Path("dados/bruto/global_ads_performance_dataset.csv")
caminho_docs = Path("docs/02_exploracao_categorias.md")

# Ler a base
df = pd.read_csv(caminho_csv)

# Colunas categóricas que queremos explorar
colunas_categoricas = ["platform", "campaign_type", "industry", "country"]

# Lista para guardar o texto da documentação
linhas_documentacao = []

linhas_documentacao.append("# Exploração de Categorias\n")
linhas_documentacao.append("Este documento lista os valores únicos encontrados nas principais colunas categóricas da base.\n")

print("=== EXPLORAÇÃO DE CATEGORIAS ===")

for coluna in colunas_categoricas:
    valores_unicos = sorted(df[coluna].unique())
    quantidade = df[coluna].nunique()

    print(f"\nColuna: {coluna}")
    print(f"Quantidade de valores únicos: {quantidade}")
    print("Valores encontrados:")
    
    linhas_documentacao.append(f"\n## {coluna}\n")
    linhas_documentacao.append(f"Quantidade de valores únicos: {quantidade}\n")
    linhas_documentacao.append("Valores encontrados:\n")

    for valor in valores_unicos:
        print(f"- {valor}")
        linhas_documentacao.append(f"- {valor}\n")

# Salvar documentação
caminho_docs.write_text("".join(linhas_documentacao), encoding="utf-8")

print("\nDocumentação gerada com sucesso!")
print(f"Arquivo salvo em: {caminho_docs}")
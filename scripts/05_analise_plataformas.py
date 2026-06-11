import pandas as pd
from pathlib import Path

# Caminhos
caminho_csv = Path("dados/bruto/global_ads_performance_dataset.csv")
caminho_docs = Path("docs/04_analise_plataformas.md")

# Ler base
df = pd.read_csv(caminho_csv)

# Agrupar por plataforma
analise = (
    df.groupby("platform")
    .agg(
        investimento=("ad_spend", "sum"),
        receita=("revenue", "sum"),
        conversoes=("conversions", "sum"),
        impressoes=("impressions", "sum"),
        cliques=("clicks", "sum")
    )
    .reset_index()
)

# KPIs calculados
analise["ROAS"] = analise["receita"] / analise["investimento"]
analise["CTR"] = analise["cliques"] / analise["impressoes"]
analise["CPA"] = analise["investimento"] / analise["conversoes"]

# Ordenar por receita
analise = analise.sort_values(
    by="receita",
    ascending=False
)

# Mostrar resultado
print("\n=== ANÁLISE POR PLATAFORMA ===\n")
print(analise)

# Salvar documentação
conteudo = "# Análise por Plataforma\n\n"
conteudo += "Comparação de desempenho entre Google Ads, Meta Ads e TikTok Ads.\n\n"

conteudo += analise.to_markdown(index=False)

caminho_docs.write_text(
    conteudo,
    encoding="utf-8"
)

print("\nDocumentação gerada com sucesso!")
print(f"Arquivo salvo em: {caminho_docs}")
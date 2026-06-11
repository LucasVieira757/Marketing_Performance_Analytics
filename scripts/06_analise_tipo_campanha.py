import pandas as pd
from pathlib import Path

# Caminhos
caminho_csv = Path("dados/bruto/global_ads_performance_dataset.csv")
caminho_docs = Path("docs/05_analise_tipo_campanha.md")

# Ler base
df = pd.read_csv(caminho_csv)

# Agrupar por tipo de campanha
analise = (
    df.groupby("campaign_type")
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

# Ordenar pela receita
analise = analise.sort_values(
    by="receita",
    ascending=False
)

# Mostrar resultado
print("\n=== ANÁLISE POR TIPO DE CAMPANHA ===\n")
print(analise)

# Gerar documentação
conteudo = "# Análise por Tipo de Campanha\n\n"
conteudo += "Comparação de desempenho entre Search, Shopping, Video e Display.\n\n"

conteudo += analise.to_markdown(index=False)

caminho_docs.write_text(
    conteudo,
    encoding="utf-8"
)

print("\nDocumentação gerada com sucesso!")
print(f"Arquivo salvo em: {caminho_docs}")
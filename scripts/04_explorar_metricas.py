import pandas as pd
from pathlib import Path

# Caminhos
caminho_csv = Path("dados/bruto/global_ads_performance_dataset.csv")
caminho_docs = Path("docs/03_exploracao_metricas.md")

# Ler a base
df = pd.read_csv(caminho_csv)

# Métricas principais
investimento_total = df["ad_spend"].sum()
receita_total = df["revenue"].sum()
impressoes_total = df["impressions"].sum()
cliques_total = df["clicks"].sum()
conversoes_total = df["conversions"].sum()

# Métricas médias
ctr_medio = df["CTR"].mean()
cpc_medio = df["CPC"].mean()
cpa_medio = df["CPA"].mean()
roas_medio = df["ROAS"].mean()

# Cálculos recalculados
ctr_calculado = cliques_total / impressoes_total
cpc_calculado = investimento_total / cliques_total
cpa_calculado = investimento_total / conversoes_total
roas_calculado = receita_total / investimento_total

# Exibir no terminal
print("=== EXPLORAÇÃO DE MÉTRICAS ===")
print(f"Investimento total: R$ {investimento_total:,.2f}")
print(f"Receita total: R$ {receita_total:,.2f}")
print(f"Impressões totais: {impressoes_total:,.0f}")
print(f"Cliques totais: {cliques_total:,.0f}")
print(f"Conversões totais: {conversoes_total:,.0f}")

print("\n=== MÉDIAS DA BASE ===")
print(f"CTR médio: {ctr_medio:.4f}")
print(f"CPC médio: R$ {cpc_medio:.2f}")
print(f"CPA médio: R$ {cpa_medio:.2f}")
print(f"ROAS médio: {roas_medio:.2f}")

print("\n=== INDICADORES RECALCULADOS ===")
print(f"CTR calculado: {ctr_calculado:.4f}")
print(f"CPC calculado: R$ {cpc_calculado:.2f}")
print(f"CPA calculado: R$ {cpa_calculado:.2f}")
print(f"ROAS calculado: {roas_calculado:.2f}")

# Criar documentação
conteudo = f"""# Exploração de Métricas

Este documento apresenta uma visão geral das principais métricas da base de campanhas.

## Totais

| Métrica | Valor |
|---|---:|
| Investimento total | R$ {investimento_total:,.2f} |
| Receita total | R$ {receita_total:,.2f} |
| Impressões totais | {impressoes_total:,.0f} |
| Cliques totais | {cliques_total:,.0f} |
| Conversões totais | {conversoes_total:,.0f} |

## Médias da base

| Métrica | Valor |
|---|---:|
| CTR médio | {ctr_medio:.4f} |
| CPC médio | R$ {cpc_medio:.2f} |
| CPA médio | R$ {cpa_medio:.2f} |
| ROAS médio | {roas_medio:.2f} |

## Indicadores recalculados

| Métrica | Fórmula | Valor |
|---|---|---:|
| CTR calculado | cliques / impressões | {ctr_calculado:.4f} |
| CPC calculado | investimento / cliques | R$ {cpc_calculado:.2f} |
| CPA calculado | investimento / conversões | R$ {cpa_calculado:.2f} |
| ROAS calculado | receita / investimento | {roas_calculado:.2f} |
"""

# Salvar documentação
caminho_docs.write_text(conteudo, encoding="utf-8")

print("\nDocumentação gerada com sucesso!")
print(f"Arquivo salvo em: {caminho_docs}")
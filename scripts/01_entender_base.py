import pandas as pd

# Caminho do arquivo CSV
caminho_arquivo = "dados/bruto/global_ads_performance_dataset.csv"

# Carregar a base
df = pd.read_csv(caminho_arquivo)

print("=== VISÃO GERAL DA BASE ===")
print(f"Linhas: {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")

print("\n=== COLUNAS ===")
print(df.columns.tolist())

print("\n=== PRIMEIRAS 5 LINHAS ===")
print(df.head())

print("\n=== TIPOS DE DADOS ===")
print(df.dtypes)

print("\n=== VALORES NULOS ===")
print(df.isnull().sum())

print("\n=== DUPLICADOS ===")
print(df.duplicated().sum())

print("\n=== RESUMO NUMÉRICO ===")
print(df.describe())
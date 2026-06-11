import pandas as pd

# Caminho do CSV original
caminho_csv = "dados/bruto/global_ads_performance_dataset.csv"

# Caminho do Excel que será criado
caminho_excel = "dados/tratado/global_ads_performance_dataset.xlsx"

# Ler o CSV
df = pd.read_csv(caminho_csv)

# Salvar como Excel
df.to_excel(caminho_excel, index=False)

print("Arquivo convertido com sucesso!")
print(f"Linhas: {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")
print(f"Arquivo salvo em: {caminho_excel}")
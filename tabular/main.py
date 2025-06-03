import pandas as pd

caminho_arquivo = "tabular/GRAPE_QUALITY.csv"

df = pd.read_csv(caminho_arquivo)

print(f"Número total de registros: {len(df)}")
print(f"Colunas no dataset:\n{df.columns.tolist()}\n")

print("Tipos de dados das colunas:")
print(df.dtypes, "\n")

print("Quantidade de valores únicos por coluna categórica:")
for col in df.select_dtypes(include=["object"]).columns:
    print(f"{col}: {df[col].nunique()} valores únicos")

print("\nEstatísticas para colunas numéricas:")
print(df.describe())

target = "variety"
print("\nValores distintos do target:")
print(df[target].unique())

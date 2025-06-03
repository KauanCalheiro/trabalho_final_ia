from sklearn.datasets import fetch_20newsgroups
import pandas as pd

newsgroups = fetch_20newsgroups(subset='all')

df = pd.DataFrame({
    'text': newsgroups.data,
    'target': newsgroups.target
})

target_names = newsgroups.target_names
df['target_name'] = df['target'].apply(lambda x: target_names[x])

print(f"Número total de registros: {len(df)}")
print(f"Colunas no dataset:\n{df.columns.tolist()}\n")

print("Tipos de dados das colunas:")
print(df.dtypes, "\n")

print("Quantidade de valores únicos por coluna categórica:")
for col in df.select_dtypes(include=['object']).columns:
    print(f"{col}: {df[col].nunique()} valores únicos")

print("\nEstatísticas para colunas numéricas:")
print(df.describe())

target = "target_name"
print("\nValores distintos do target:")
print(df[target].unique())
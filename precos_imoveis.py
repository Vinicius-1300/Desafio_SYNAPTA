import pandas as pd
import numpy as np
import plotly as plt

analise_precos = pd.read_csv(r"c:\Users\Vinicius\Desktop\Pasta Pessoal\Projetos GitHub\Desafio_SYNAPTA\data.csv", encoding="utf-8", low_memory=False)
print(analise_precos.rename(columns={'address': 'Endereço', 'district': 'Bairro', 'area': 'Área', 'bedrooms': 'Quartos', 'garage': 'Garagem', 'type': 'Tipo', 'rent': 'Aluguel', 'total': 'Total'}))
print("=" * 21, "RESUMO ANALÍTICO E ESTATÍSTICO", "=" * 21)
print(analise_precos.describe()) #describe(): função que retorna um resumo do dateset, de forma mais estatística
print("=" * 75)

print("=" * 10, "PREÇO MÉDIO", "=" * 10)
preco_medio = analise_precos['rent'].mean()
print(f"Preço médio do aluguel: R$ {preco_medio:.2f}")

print("=" * 10, "PREÇO MEDIANO" , "=" * 10)
mediana = analise_precos['rent'].median()
print(f"Preço mediano: R$ {mediana:.2f}")

maior_aluguel = analise_precos.groupby('address')['rent'].max()
menor_aluguel = analise_precos.groupby('address')['rent'].min()
print(f"Localidades com maiores alugueis: {maior_aluguel}")
print("/" * 60)
print(f"Localidades com menores alugueis {menor_aluguel}")
print("/" * 60)

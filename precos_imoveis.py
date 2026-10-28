import pandas as pd
import plotly.express as px

analise_precos = pd.read_csv(r"c:\Users\Vinicius\Desktop\Pasta Pessoal\Projetos GitHub\Desafio_SYNAPTA\data.csv", encoding="utf-8", low_memory=False)
analise_precos = analise_precos.rename(columns={'address': 'Endereço', 'district': 'Bairro', 'area': 'Área', 'bedrooms': 'Quartos', 'garage': 'Garagem', 'type': 'Tipo', 'rent': 'Aluguel', 'total': 'Total'})
print(analise_precos)
print("=" * 21, "RESUMO ANALÍTICO E ESTATÍSTICO", "=" * 21)
print(analise_precos.describe()) #describe(): função que retorna um resumo do dateset, de forma mais estatística
print("=" * 75)

print("=" * 10, "PREÇO MÉDIO", "=" * 10)
preco_medio = analise_precos['Aluguel'].mean()
print(f"Preço médio do aluguel: R$ {preco_medio:.2f}")

print("=" * 10, "PREÇO MEDIANO" , "=" * 10)
mediana = analise_precos['Aluguel'].median()
print(f"Preço mediano: R$ {mediana:.2f}")

maior_aluguel = analise_precos.groupby('Endereço')['Aluguel'].max()
menor_aluguel = analise_precos.groupby('Endereço')['Aluguel'].min()
print(f"Localidades com maiores alugueis: {maior_aluguel}")
print("/" * 60)
print(f"Localidades com menores alugueis {menor_aluguel}")
print("/" * 60)

analise_area_aluguel = analise_precos[['Área', 'Aluguel']].head(100)
grafico = px.scatter(analise_area_aluguel, x='Área', y='Aluguel', color='Aluguel', title='Valor do aluguel pela área')
grafico.show()

analise_aluguel_endereco = analise_precos[['Aluguel', 'Endereço']].head(40)
grafico2 = px.bar(analise_aluguel_endereco, x='Aluguel', y='Endereço', title="Valor do aluguel pela localidade", color='Endereço')
grafico2.show()

analise_tipo = analise_precos[['Aluguel', 'Tipo']].head(40)
analise_tipo = analise_tipo.sort_values(by='Aluguel', ascending=True)
grafico3 = px.bar(analise_tipo, x='Aluguel', y='Tipo', title='Aluguel x Tipo', color='Tipo')
grafico3.show()
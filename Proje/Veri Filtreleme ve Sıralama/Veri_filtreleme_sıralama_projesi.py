import pandas as pd
import numpy as np


data = pd.read_csv('country.csv')
data = data.replace(',', '.', regex=True)


numeric_cols = ['Population', 'Area (sq. mi.)', 'Pop. Density (per sq. mi.)',
                'GDP ($ per capita)', 'Literacy (%)']
for col in numeric_cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')


# 1. Görev:
print("\n1. Nüfusa göre azalan sıralama:")
print(data[['Country', 'Population']].sort_values(by='Population', ascending=False).head(10))


# 2. Görev: 
print("\n2. GDP per capita’ya göre artan sıralama:")
print(data[['Country', 'GDP ($ per capita)']].sort_values(by='GDP ($ per capita)', ascending=True).head(10))


# 3. Görev: 
print("\n3. Nüfusu 10 milyonun üzerinde olan ülkeler:")
print(data[data['Population'] > 10_000_000][['Country', 'Population']].head(10))


# 4. Görev: 
print("\n4. Literacy oranına göre en yüksek 5 ülke:")
print(data[['Country', 'Literacy (%)']].sort_values(by='Literacy (%)', ascending=False).head(5))


# 5. Görev: 
print("\n5. GDP per capita > 10.000 olan ülkeler:")
print(data[data['GDP ($ per capita)'] > 10000][['Country', 'GDP ($ per capita)']].head(10))


# 6. Görev:
print("\n6. Nüfus yoğunluğu en yüksek ilk 10 ülke:")
print(data[['Country', 'Pop. Density (per sq. mi.)']].sort_values(by='Pop. Density (per sq. mi.)', ascending=False).head(10))



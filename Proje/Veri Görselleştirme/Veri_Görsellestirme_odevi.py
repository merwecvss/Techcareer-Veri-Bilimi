import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('50_Startups.csv')
data.head()


# 1.GÖREV: 
plt.figure(figsize=(6,4))
plt.scatter(data["R&D Spend"], data["Profit"], color="blue")
plt.xlabel("R&D Harcaması")
plt.ylabel("Kâr")
plt.title("R&D Harcaması ile Kâr İlişkisi")
plt.show()


# 2.GÖREV: 
plt.figure(figsize=(6,4))
plt.scatter(data["Administration"], data["Profit"], color="green")
plt.xlabel("Yönetim Harcaması")
plt.ylabel("Kâr")
plt.title("Yönetim Harcaması ile Kâr İlişkisi")
plt.show()


# 3. GÖREV: 
plt.figure(figsize=(6,4))
state_profit = data.groupby("State")["Profit"].mean()
state_profit.plot(kind="bar", color=["orange","purple","cyan"])
plt.xlabel("Eyalet")
plt.ylabel("Ortalama Kâr")
plt.title("Eyaletlere Göre Ortalama Kârlar")
plt.show()


# 4. GÖREV: 
plt.figure(figsize=(8,5))
data[["R&D Spend", "Administration", "Marketing Spend"]].boxplot()
plt.title("Harcama Türlerinin Dağılımı")
plt.ylabel("Tutar")
plt.show()
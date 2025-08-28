myList = [12, 4, 9, 25, 30, 7, 18]

toplam = 0
for i in myList:
    toplam += i

ortalama = toplam / len(myList)
print(f"Listenin Ortalaması: {ortalama}")

buyukSayilar = []
for sayi in myList:
    if sayi > ortalama:
        buyukSayilar.append(sayi)
print(f"Listedeki Ortalamadan büyük sayılar {buyukSayilar}")



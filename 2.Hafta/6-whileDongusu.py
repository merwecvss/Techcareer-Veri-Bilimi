toplam = 0
adet = 0

while True:
    sayi = int(input("Bir Sayı Giriniz: "))
    if sayi == 0:
        break
    toplam += sayi
    adet += 1

if adet > 0:
    ortalama = toplam / adet
    print(f"Girilen sayıların toplamı: {toplam}")
    print(f"Girilen sayıların ortalaması: {ortalama}")
else:
    print("Toplanacak Bir Sayı Girmediniz.")

dogumYili = int(input("Doğum Yılınızı Giriniz:"))
mevcutYil = 2025
yas = mevcutYil - dogumYili

if  0<= yas <= 12:
    print("Çocuksunuz")
elif 13<= yas <= 17:
    print("Ergensiniz")
elif yas >= 18:
    print("Yetişkinsiniz")
else:
    print("Doğum Yılınızı Yanlış Girdiniz.")

sifre = input("Lütfen Şifrenizi Girin: ")

uzunluk = len(sifre) >= 8
buyuk_harf = False
rakam = False

for harf in sifre:
    if harf.isupper():
        buyuk_harf = True
    if harf.isdigit():
        rakam = True

if uzunluk == True:
    print("Şifreniz geçerli")

else:
    print("Şifreniz geçersiz")
    if uzunluk == False:
        print("- Şifre en az 8 karakter olmalı")
    if buyuk_harf == False:
        print("- Şifre en az 1 büyük harf içermeli")
    if rakam == False:
        print("- Şifre en az 1 rakam içermeli")

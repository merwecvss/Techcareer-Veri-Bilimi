sayi = int(input("Bir Sayı Giriniz: "))

if sayi > 0:
    if sayi%2==0:
        print("Girilen Sayı Pozitif ve Çifttir.")
    else:
        print("Girilen Sayı Pozitif ve Tektir.")
elif sayi <0:
    if sayi%2==0:
        print("Girilen Sayı Negatif ve Çiftir .")
    else:
        print("Girilen Sayı Negatif ve Tektir.")
else:
    print("Girilen Sayı 0'a eşittir.")
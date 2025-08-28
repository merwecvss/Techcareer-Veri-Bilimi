kelime = str(input("Lütfen Bir Kelime Giriniz: "))
kelime = kelime.upper()

sozluk = {}

for harf in kelime:
    if harf.isalpha():
        if harf in sozluk:
            sozluk[harf] += 1
        else:
            sozluk[harf] = 1

harfFrekans = [{"harf": h, "adet": a} for h, a in sozluk.items()]

print(harfFrekans)
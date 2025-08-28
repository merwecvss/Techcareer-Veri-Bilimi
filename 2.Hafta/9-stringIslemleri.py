buyukKelime = ""
cumle = str(input("Lütfen Cümlenizi Giriniz: "))
kelimeler = cumle.split()
for kelime in kelimeler:
    buyukKelime += (" " + kelime.capitalize())
print(buyukKelime)
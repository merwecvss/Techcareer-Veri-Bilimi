fiyat = float(input("Ürünün Fiyatını Giriniz: "))
indirimOrani = int(input("İndirim Oranını (yüzde) Giriniz: "))

indirimTutari = 100 - indirimOrani

indirimliFiyat = fiyat * indirimTutari /100

print(indirimliFiyat)
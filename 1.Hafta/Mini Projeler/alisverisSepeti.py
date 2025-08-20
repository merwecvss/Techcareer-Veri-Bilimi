urun1 = int(input("1. Ürünün Fiyatını Giriniz:"))
urun2 = int(input("2. Ürünün Fiyatını Giriniz:"))
urun3 = int(input("3. Ürünün Fiyatını Giriniz:"))

toplamFiyat = urun1 + urun2 + urun3
indirimliFiyat = toplamFiyat * 0.9

if toplamFiyat > 200:
    print("İndirim Uygulanmadan Fiyatınız: {} \nİndirimli Fiyatınız:{}" .format(toplamFiyat,indirimliFiyat))
else:
    print("Aldığınız Ürümlerde İndirim Uygulanmamıştır. \nÖdeyeceğiniz Ücret: {}".format(toplamFiyat))
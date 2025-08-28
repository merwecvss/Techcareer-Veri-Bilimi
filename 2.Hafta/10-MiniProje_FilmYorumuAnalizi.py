yorumlar = []
print("""
    Kullanıcı Yorum Sayfasına Hoşgeldiniz.
    Burada Yorum Yapabilir ve Yaptığınız Yorumları Analiz Edebilirsiniz.
    Hazırsanız Başlayalım.
    Unutmayın Yorum Eklemeden Çıkmak İçin q Harfine Basmanız Yeterli Olacaktır.
    """)
while True:
    girdi = input("Yorumunuzu Giriniz: ")
    if girdi == "q":
        break
    yorumlar.append(girdi)

olumlu_yorum_say = 0
olumsuz_yorum_say = 0
toplam_uzunluk = 0
uzun_yorum = ""
kisa_yorum = ""

if yorumlar:
    uzun_yorum = kisa_yorum = yorumlar[0]

    for yorum in yorumlar:
        uzunluk = len(yorum)
        toplam_uzunluk += uzunluk

        if uzunluk > len(uzun_yorum):
            uzun_yorum = yorum
        if uzunluk < len(kisa_yorum):
            kisa_yorum = yorum

        if "iyi" in yorum.lower():
            olumlu_yorum_say += 1

        if "kötü" in yorum.lower():
            olumsuz_yorum_say += 1

    ortalama = toplam_uzunluk / len(yorumlar)

    print("\nToplam yorum sayısı:", len(yorumlar))
    print("\"iyi\" kelimesi geçen yorum sayısı:", olumlu_yorum_say)
    print("\"kötü\" kelimesi geçen yorum sayısı:", olumsuz_yorum_say)
    print("En uzun yorum:", uzun_yorum)
    print("En kısa yorum:", kisa_yorum)
    print(f"Ortalama uzunluk: {ortalama:.1f} karakter")
else:
    print("Hiç yorum girilmedi.")

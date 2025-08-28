kelime = str(input("Bir Kelime Giriniz: "))
kelime = kelime.upper()
if kelime == kelime[::-1]:
    print("Girilen Kelime Palindromdur.")

else:
    print("Girilen Kelime Palindrom Değildir.")
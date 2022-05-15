import random
karakterler= "qwertyuıopasdfghjklzxcvbnmiIQWERTYUOPASDFGHJKLZXCVBNM1234567890é!'^+%&/()=?_-*<>£#$½{[]}"
sifresayisi = int(input("olusturmak istediginiz sifre sayisini giriniz "))
for x in range(sifresayisi):
    sifre = ""
    for x in range(16):
        karakter = random.choice(karakterler)
        sifre = sifre + karakter
    print("Random Sifreniz : ", sifre)


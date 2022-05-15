import random
sayi =random.randint(0,28)
girilenler = []
denemesayisi=0
while True:
    for x in range(3):
        y = int(input("bir rakam giriniz"))
        girilenler.append(y)
    a = girilenler[-3]
    b = girilenler[-2]
    c = girilenler[-1]
    if a+b+c == sayi :
        print("tebrikler oyunu kazandınız")
        denemesayisi +=1
        print("deneme sayınız ", denemesayisi)
        break
    else:
        print("tekrar deneyiniz")
        denemesayisi +=1
    print("deneme sayınız ",denemesayisi)




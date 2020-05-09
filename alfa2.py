# Alfabetik değer; bir sayı yazıyla yazıldığında onu oluşturan
# tüm harflerin Türkçe alfabesindeki sıralarının toplamıdır.

def alfa_deger(x) :
    birler = [0,35,38,30,69,31,51,51,73,91]
    onlar = [0,35,89,96,60,48,90,109,87,77]
    yuz = 83

    yuz_bas = (x // 100) % 10
    on_bas = (x // 10) - (yuz_bas * 10)
    bir_bas = x % 10

    y = birler[bir_bas] + onlar[on_bas]
    if x >= 100 and x < 200 :
        y = y + yuz
    if x >= 200 :
        y = y + birler[yuz_bas] + yuz

    return y

for i in range(999) :
    if i > alfa_deger(i) :
        print (i, "sayisinin alfabetik değeri:", alfa_deger(i))
        break

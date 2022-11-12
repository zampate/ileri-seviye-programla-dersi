#= 0 girilene kadar klavyeden tam sayı değerler alın, bu sayılardan en büyüğü ile en küçüğünü bulan ve ekranda gösteren python kodu

sayilar = []

while True:
    sayi = int(input("sayı giriniz"))
    if sayi == 0:
        break
    sayilar.append(sayi)

en_kucuk = min(sayilar)
en_buyuk = max(sayilar)

print("Liste İçindeki En Büyük Sayı :", en_buyuk, "\nListe İçindeki En Kücük Sayı :", en_kucuk)

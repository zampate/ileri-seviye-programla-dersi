#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)
print(faktoriyel(5))  # 1

def ortalama_disi_aktar(dizi):
    ortalama = sum(dizi) / len(dizi)
    disi = [sayi for sayi in dizi if sayi < ortalama or sayi > ortalama]
    return disi
print(ortalama_disi_aktar([1, 2, 3, 4, 5])) 

liste = [ 'GeeksforGeeks' , 'Geeky' , 'Bilgisayarlar' , 'Algoritmalar' ]
aranan = input ( "aranan harfi giriniz" )
def  metin_ara (liste,a):
     liste1 = [x for x in liste if aranan in x ]  
     return liste1
print(len(metin_ara(liste,aranan)))  


cumle = "Belirli bir düzende otomatik listeler oluşturmak için liste üreteçleri kullanılır."
karakter_sayisi = int(input("Karakter sayısını girin" ))
def  bul (cumle ,a):    
    liste = cumle .split ( " " )
    for i   in liste :
          if len(i) >a:
            print (i)          
bul (cumle , karakter_sayisi)


def faktoriyel(a):
    carpim=1
    for i in range(1,a+1):
        carpim=carpim*i
    print (carpim)
    
faktoriyel(6)

metins="RETRUN deger döndürür"
def string_kontol(x):
    buyuk=[]
    kucuk=[]
    for i in x:
        if i.upper():
            buyuk.append(i)
        elif i.lower():
            kucuk.append(i)
        else:
            pass
    return kucuk,buyuk
s1,s2=string_kontol(metins)
print("küçük harf",s1)
print("büyük harf",s2)


def ters_çevir(s):
    x=""
    index=len(s)
    while index>0:
        x+=s[index-1]
        index=index-1
    return x
print(ters_çevir("123sdfgh"))

def mükemmelsayı(a):
 toplam=0   
 for i in range(1,a):
    if(a%i == 0):
        toplam +=i
        
    if(a == toplam):
     print("Mükemmel Sayidir.")
    else:
     print("Mükemmel Sayi Degildir")
'''
''' 
def faktoriyel(a):
    carpim=1
    for i in range(1,a+1):
     carpim *=i
     return(carpim)
     return a * faktoriyel(carpim)

def us_al(taban,us):
    carpim=1
    for i in range(1,us+1):
        carpim*=taban
    print(carpim)
us_al(5,3)

def usal(taban,us):
    if taban==1:
        return 1
    elif us==0:
        return 1
    else :
        return taban*usal(taban, us-1)
    
print(us_al(5, 3))

def faktoriyel(n):
   if n==0:
       return 1
   elif n==1:
       return 1
   else:
       return n*faktoriyel(n-1)
sayi1=int(input("sayı giriniz"))
fak=faktoriyel(sayi1)
print(faktoriyel)


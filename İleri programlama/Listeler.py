#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as rn
liste=[]
toplam=0
for i in range(0,10):
    sayi=rn.randint(0,100)
    liste.append(sayi)
eleman_sayisi=len(liste)
for i in range(0,eleman_sayisi):
    toplam=toplam+liste[i]
ortalama=toplam/eleman_sayisi
ortalama_ustu=[]
for i in range(0,10):
    if liste[i]>ortalama:
        ortalama_ustu.append(liste[i])
print(liste)
print(ortalama)
print(ortalama_ustu)
'''
'''
import random as rn
liste1=[]
toplam=0
for i in range(0,10):
    sayi=rn.randint(0,100)
    liste1.append(sayi)
print(liste1)
liste1.sort(reverse=False)
print(liste1)


cumle="Belirli bir düzende otomatik listeler oluşturmak için liste üreteçleri kullanılır."
kelime=cumle.split(" ")
for i in kelime:
    if len(i)>7:
        print(i)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[3]:


saat=int(input("Saat giriniz"))

if saat<=1:
    para=saat*5
    print("Ödemeniz gereken miktar=",para,"TL")
elif saat<=5:
    para=saat*4
    print("Ödemeniz gereken miktar=",para,"TL")
elif saat>5:
    para=saat*3
    print("Ödemeniz gereken miktar=",para,"TL")
    


# In[6]:


türkcekarakterler="çğıİöşü"
parola=input("Oluşturmak istediğiniz parolayı yazınız")
for harf in parola:
 if harf in türkcekarakterler:
        print("Türkçe karakter kullandınız:", harf)


# In[7]:


vize=float(input("Vize Notunuzu Giriniz"))
final=float(input("Final Notunuzu Giriniz"))
ortalama=vize*0.4+final*0.6
print("Ortalamanız=",ortalama)


# In[12]:


vize=float(input("Vize Notunuzu Giriniz"))
final=float(input("Final Notunuzu Giriniz"))
ortalama=vize*0.4+final*0.6
if ortalama<50:
    print("Kaldınız")
    print("Ortalamanız=",ortalama)
else:
    print("Geçtiniz")
    print("Ortalamanız=",ortalama)


# In[18]:


sayilar=[]
while True:
 sayi=int(input("Sayı giriniz"))
 if sayi==0:
  break
 sayilar.append(sayi)
    
    
enkucuk=min(sayilar)  
enbuyuk=max(sayilar)
print("En büyük sayı=",enbuyuk,"Enkucuk sayı=",enkucuk)


# In[19]:


metin=input("Kelime gir")
print(len(metin))


# In[21]:


a=5
b=9
c=a**b
print(a,"üzeri",b,"=",c)


# In[22]:


sayi1=int(input("sayi giriniz"))
sayi2=int(input("Sayi giriniz"))
ortalama=(sayi1+sayi2)/2
print("Sayıların ortalaması=",ortalama)


# In[ ]:





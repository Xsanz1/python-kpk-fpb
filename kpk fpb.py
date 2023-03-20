#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def hitung_fpb(a, b):
    if b == 0:
        return a
    else:
        return hitung_fpb(b, a % b)

def hitung_kpk(a, b):
    kpk = max(a, b)
    while True:
        if kpk % a == 0 and kpk % b == 0:
            return kpk
        else:
            kpk += 1

while True:
    print("Pilihan:")
    print("1. Hitung FPB")
    print("2. Hitung KPK")
    print("3. Keluar")
    
    pilihan = int(input("Masukkan pilihan Anda: "))
    
    if pilihan == 1:
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan kedua: "))
        fpb = hitung_fpb(a, b)
        print("FPB dari", a, "dan", b, "adalah", fpb)
    elif pilihan == 2:
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan kedua: "))
        kpk = hitung_kpk(a, b)
        print("KPK dari", a, "dan", b, "adalah", kpk)
    elif pilihan == 3:
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")


# In[ ]:





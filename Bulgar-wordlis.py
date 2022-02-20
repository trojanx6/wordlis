#python
#instagram: dridex_trojan_lockbit

#lisans apache 2.0 
import random as r 
sem = "~`|•√π÷×¶∆£€$¢^°={}\%©®@#₺_&-+()/*"':;!?q<>'
harf = "АаБбВвГгДдЕеЖжб В Г Д ЕЗзИЙйКкЛлМмНнОПпРЗдравейте приятелирСсТтУуФХхЦцЧШшЩщЪъЬьЮюЯ1"
sayi = "1234567890_-*#"
karisik = 'АаБбВвГгДдЕеЖжЗзИЙйКкЛлМмНнОПпРрСсТтУуФХхЦцЧШ б В Г Д ЕшЩщЪъЬьЗдравейте приятелиЮюЯ1234567890@#₺_&-+()/*!?;:.,~|•√π÷×¶∆£€$¢^°={\%][✓<>'

print("""
[1] символ
[2] дума
[3] номер
[4] смесени
автор на кода на троянски кон  """)

print("-"*30)

def symbol():
    a = 0
    dosya_ = open("wordlis1..txt","w")
    kac_1 = int(input("брой линии: "))
    while a < kac_1:
        a += 1
        uzun = r.randint(1,10)
        cikti=   ''.join(r.sample(sem,uzun) )
        dosya_.write(cikti)
        dosya_.write("\n")
        if a == kac_1:
            dosya_.close()
            break

def letters():
    s = 0
    _dosya = open("wordlis2.txt","w")
    kac2 = int(input("брой линии: "))
    while s < kac2:
        s += 1
        uzun1 = r.randint(1,10)
        cikti1 = ''.join(r.sample(harf,uzun1))
        _dosya.write(cikti1)
        _dosya.write("\n")
        if s == kac2:
            _dosya.close()
            break

def number():
    d = 0
    dosya = open("wordlis3.txt", "w")
    kac = int(input("брой линии: "))
    while d < kac:  
        d += 1 
        uzun2 = r.randint(1,14)
        cikti2 = ''.join(r.sample(sayi,uzun2))
        dosya.write(cikti2)
        dosya.write("\n")
        if d == kac:
            dosya.close()
            break


def all():
    f = 0
    dosya1 = open("wordlis4.txt","w")
    kac3 = int(input("брой линии: "))
    while f < kac3:
        f += 1
        uzun3 = r.randint(1,21)
        cikti3 = ''.join(r.sample(karisik,uzun3))
        dosya1.write(cikti3)
        dosya1.write("\n")
        if f == kac3:
            dosya1.close()
            break


islem = int(input("въведете селекция: "))
    
if islem == 1:
   print(symbol())
elif islem == 2:
     print(letters())
elif islem == 3:
    print(number())
elif islem == 4:
    print(all())

#python
#instagram: dridex_trojan_lockbit

#lisans apache 2.0 
import os, time
from colorama import Fore
F = Fore
import random as r 
os.system("clear")
sem = "~`|•√π÷×¶∆£€$¢^°={}\%©®@#₺_&-+()/*"':;!?q<>'
harf = "qwertyuiopasdfghjklzxcvbnmQWERTYUİOPASDFGHJKLZXCVBNM1"
sayi = "1234567890_-*#"
karisik = 'qwertyuiopasdfghjklzxcvbnmQWERTYUİOPASDFGHJKLZXCVBNM1234567890@#₺_&-+()/*!?;:.,~|•√π÷×¶∆£€$¢^°={\%][✓<>'
print(F.RED+"""
 __      __                .___.__  .__          __    
/  \    /  \___________  __| _/|  | |__| _______/  |_  
\   \/\/   /  _ \_  __ \/ __ | |  | |  |/  ___/\   __\ 
 \        (  <_> )  | \/ /_/ | |  |_|  |\___ \  |  |   
  \__/\  / \____/|__|  \____ | |____/__/____  > |__|   
       \/                   \/              \/         

	Coded By = Trojan / Designed By = Furkan Kerem
"""+F.RESET)
print(F.BLUE+'[ '+F.RESET+'1'+F.BLUE+' ] '+F.BLUE+' [ '+F.RESET+'Sembol / Symbol'+F.BLUE+' ]'+F.RESET)
print("\n")
print(F.BLUE+'[ '+F.RESET+'2'+F.BLUE+' ] '+F.BLUE+' [ '+F.RESET+'Harf / Letters'+F.BLUE+' ]'+F.RESET)
print("\n")
print(F.BLUE+'[ '+F.RESET+'3'+F.BLUE+' ] '+F.BLUE+' [ '+F.RESET+'Sayı / Number'+F.BLUE+' ]'+F.RESET)
print("\n")
print(F.BLUE+'[ '+F.RESET+'4'+F.BLUE+' ] '+F.BLUE+' [ '+F.RESET+'Hepsi / All '+F.BLUE+' ]'+F.RESET)
print("\n")
print(F.BLUE+'[ '+F.RESET+'5'+F.BLUE+' ] '+F.BLUE+' [ '+F.RESET+'Çıkış / Exit'+F.BLUE+' ]'+F.RESET)
print("\n")

def symbol():
    a = 0
    dosya_ = open("wordlis1.txt","w")
    kac_1 = int(input(F.RED+'[ '+F.RESET+'*'+F.RED+' ] '+F.BLUE+' [ '+F.RESET+'Satır Sayısı / Number of Rows '+F.BLUE+' ]'+F.RED+' : '+F.RESET))
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
    kac2 = int(input(F.RED+'[ '+F.RESET+'*'+F.RED+' ] '+F.BLUE+' [ '+F.RESET+'Satır Sayısı / Number of Rows '+F.BLUE+' ]'+F.RED+' : '+F.RESET))
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
    kac = int(input(F.RED+'[ '+F.RESET+'*'+F.RED+' ] '+F.BLUE+' [ '+F.RESET+'Satır Sayısı / Number of Rows '+F.BLUE+' ]'+F.RED+' : '+F.RESET))
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
    kac3 = int(input(F.RED+'[ '+F.RESET+'*'+F.RED+' ] '+F.BLUE+' [ '+F.RESET+'Satır Sayısı / Number of Rows '+F.BLUE+' ]'+F.RED+' : '+F.RESET))
    while f < kac3:
        f += 1
        uzun3 = r.randint(1,21)
        cikti3 = ''.join(r.sample(karisik,uzun3))
        dosya1.write(cikti3)
        dosya1.write("\n")
        if f == kac3:
            dosya1.close()
            break


islem = input(F.RED+'[ '+F.RESET+'*'+F.RED+' ] '+F.BLUE+' [ '+F.RESET+'Seçim Yapınız / Choose '+F.BLUE+' ]'+F.RED+' : '+F.RESET)

if islem == "1":
   print(symbol())
elif islem == "2":
     print(letters())
elif islem == "3":
    print(number())
elif islem == "4":
    print(all())
elif islem == "5":
    os.system("clear")
else:
    print(F.BLUE+'[ '+F.RESET+'!'+F.BLUE+' ] '+F.BLUE+' [ '+F.RESET+'Hatalı Seçim / Wrong Choice'+F.BLUE+' ]'+F.RESET)

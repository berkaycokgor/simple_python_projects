import time
import urllib.request

while True:
        try:
            a = input("Resim indirmeye başlamak için 1'e, çıkmak için 2'ye basınız.")
            if a=="1":
        
                url = input("İndirilmesini istediğiniz resmin linkini verin.\n")
                isim = input("dosyanın ismini yazın.\n")

                urllib.request.urlretrieve(url,isim + ".jpg")
                print("Resminiz indiriliyor.")
                time.sleep(1)
                print("Resminiz indirildi!")
                time.sleep(1)
                print("Program kapanıyor...")
                time.sleep(1)
                break
            elif(a=="2"):
                print("Çıktınız.")
                time.sleep(1)
                print("Program kapanıyor...")
                time.sleep(1)
                break
            else:
                print("Lütfen geçerli bir değer giriniz.")

        except ValueError:
         print("Lütfen geçerli bir değer giriniz.")

    

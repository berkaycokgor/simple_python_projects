import os
while True:
           x =int(input("CPU NU % KAÇ SEVMİYORSUN?"))
           if(x>100):
                      print("Yüzde diye sorduk.Şimdi bir daha cevapla")
                      continue
           else:
                      cpuburn = x*1000000+1
                      os.chdir("C:/Users/Q/Desktop")
                      os.mkdir("Hello EVERYBUDDY")
                      os.chdir("C:/Users/Q/Desktop/Hello EVERYBUDDY")
                      for i in range(0,cpuburn):
                                 os.mkdir("hello, number of this file is "+str(i))
           break          
           
           

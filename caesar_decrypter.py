#Please report me if you realize that there is a bug etc.
print("Caesar Cypher Decrypter #for english alphabet")
def makelist(x): #First makes the text a string for easier process
    list = []
    for i in range(0,len(x)):
        list.append(x[i])
    return list
def UpCaseCtrl(list): #Uppercase Letter Fixer
    for p in range(0,len(list)):
        asctrl = ord(list[p])
        if(asctrl<65 or (asctrl>91 and asctrl<97) or asctrl>122):
            return False #Shutdowns the program if text has a character that is not from the english alphabet
        if (asctrl>=65 and asctrl<91):
            list[p]= chr(asctrl+32)
    return list
def Decrypter(): #Main Function
    x = input("Please enter the encrypted text: ")
    list = UpCaseCtrl(makelist(x))
    for i in range(0,25):
        for q in range(0,len(x)):
            asciii = ord(list[q])

            list[q] = chr(asciii + 1)
            if (asciii == 32):
                continue
            asc= ord(list[q])
            if(asc>=122):        #if alphabet has to return back
                list[q] = chr((asc+7)%26+97)

        for h in range(0,len(list)):
            decrypted= ''.join(list)
        print(decrypted)
while True:
    Decrypter()







message = input("Enter a message : ")
cle=3

acrypter=message.upper()
lg=len(acrypter)
message=""

for i in range(lg):
    if acrypter[i]==' ':
        message+=' '
    else:
        asc=ord(acrypter[i])+cle
        message+=chr(asc+26*((asc<65)-(asc>90)))

print (message)


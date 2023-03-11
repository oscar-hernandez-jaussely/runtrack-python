L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

L2 = []


for num in L:
    if num%2 == 0:
        L2.append(num)
    

list_length=len(L2)

sum = 0

for i in range(list_length):
    sum=sum+L2[i]

print ("La liste des valeurs paires est : " +str(L2))
print ("La somme de cette liste est : " +str(sum))


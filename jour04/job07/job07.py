
L = [8, 24, 48, 2, 16]
L2 = []

for num in L:
    if num%3 == 0:
        L2.append(num)

print ("Il y a {} multiples de 3 dans cette liste " .format(len(L2)))



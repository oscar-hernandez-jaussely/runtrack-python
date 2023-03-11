
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
L2 = []

import math

for num in L:

    if num >= 25 and num <= 90:
        L2.append(num)

r = math.prod(L2)


print ("Le résultat est : " +str(r))


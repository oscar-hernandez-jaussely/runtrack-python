
def triangle (a, b, c):

    a = float(input("Longueur A : "))
    b = float(input("longueur B : "))
    c = float(input("longueur C : "))

    lst = [(a), (b), (c)]
    print (lst)

    lst.sort()
    print(lst)

    g1 = lst[2]
    print ("grandeur 1 = " +str(g1))

    g2 = lst[1]
    print ("grandeur 2 = " +str(g2))

    g3 = lst[0]
    print ("grandeur 3 = " +str(g3))

    if g1 < (g2 + g3):
        print ("Il est possible de construire un triangle avec ces valeurs")
    else:
        print ("Il n'est pas possible de construire un triangle avec ces valeurs")

    g1_carre = g1*g1
    g2_carre = g2*g2
    g3_carre = g3*g3

    if g1 < (g2 + g3):
        if g1 == g2 and not g2 == g3:
            print ("C'est un triangle isocèle")
        elif g2 == g3 and not g1 == g2:
            print ("c'est un triangle isocèle")        
        elif g1_carre == g2_carre + g3_carre:
            print("C'est un triangle rectangle")
        else:
            print ("C'est un triangle quelconque")


triangle(0, 0, 0,)


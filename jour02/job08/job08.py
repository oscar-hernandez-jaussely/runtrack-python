
def f1 (type, saison):

    type = input("type = ")
    saison = input("saison = ")

    if type == ("fruits") and saison == ("hiver"):
        print ("orange, mandarine et kiwi")

    if type == ("fruits") and saison == ("ete"): 
        print ("poire, fraise, cassis")

    if type == ("legume") and saison == ("hiver"):
        print ("carotte, topinambour, endive")

    if type == ("legume") and saison == ("ete"):
        print ("artichaut, aubgergine, navet")

f1 (0, 0)


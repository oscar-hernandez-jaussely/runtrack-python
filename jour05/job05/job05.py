
def f1 ():
    
    h = int(input("Quelle est la hauteur d'une marche (en cm) ? "))
    m = int(input("Combien y a-t-il de marches ? "))

    t  = m * h * 2

    j = t * 5

    s = j * 7

    r = s / 100

    print ("Pour {} marches de {} cm, le gardien parcours {} m par semaine." .format(m, h, r))

f1()

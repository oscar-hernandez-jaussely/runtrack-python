
def notation ():

    import random

    notes = []
 
    num = 10
    start = 0
    end = 101

    for J in range(num):
        notes.append(random.randint(start, end))

    notes.sort()

    print("Les notes des élèves sont {}" .format(notes))

    notes2 =[]
    notes3 = []

    for num in notes:
        if num < 40:
            print("{}/100 : l'élève a échoué le test" .format(num))
            notes3.append(num)
        elif num > 40:
            print("{}/100 : l'élève a réussi le test" .format(num))
            notes2.append(num)

    for num in notes2:

        if (num + (5 - num) % 5) > num :
            notes3.append(num + (5 - num) % 5)
        else:
            notes3.append(num)

    notes3.sort()

    print("Une fois arrondies, les notes des élèves sont {}" .format(notes3))


notation()


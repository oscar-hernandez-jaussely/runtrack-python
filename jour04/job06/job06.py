
l = [1, 2, 3, 4, 5]

l.insert(-1, l.pop(0))
l.insert(0, l.pop(-1))

print (l)


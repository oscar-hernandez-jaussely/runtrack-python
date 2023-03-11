
def draw_rectangle(n):

    print("+" ,"-" * (n-2),"+")

    for i in range(n-2):
        print("|", "#" * (n-3-i) + " "+ "#" * i,"|")

    print("+" ,"-" * (n-1),"+")

draw_rectangle(eval(input("Enter a value : ")))


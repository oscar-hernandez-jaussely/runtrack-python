
width = int(input("Enter rectangle width : "))
height = int(input("Enter rectangle height : "))

height_real = height - 3
height_n = height_real - 1


print("|" + "-" * width + "|")

print((("|" + " " * width + "| \n") * height_real) + "|" + " " * width + "|")

print("|" + "-" * width + "|")
      

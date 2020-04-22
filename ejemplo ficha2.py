lad1=float(input("Longitud del lado 1: "))
lad2=float(input("Longitud del lado 2: "))
lad3=float(input("Longitud del lado 3: "))

p= lad1+lad2+lad3
print("Perimetro es: ", p)

if lad1>lad2>lad3>0:
    print("Vale")
else:
    print("Falla")

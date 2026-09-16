#formato simples, sem resultados de números imaginários (complexos)
a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))
c = float(input("Insira o valor de C: "))

delta = (b**2) - 4 * a * c

x1 = (-b + (delta**(1/2))) / (2 * a)
x2 = (-b - (delta**(1/2))) / (2 * a)

print("x1 = %-5.2f" % x1)

print("x2 = %-5.2f" % x2)



#formato com importação de library e números imaginários no resultado
#estudar mais esse item

import cmath

a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))
c = float(input("Insira o valor de C: "))

delta = (b**2) - 4 * a * c

x1 = complex(-b + (delta**(1/2))) / (2 * a)
x2 = complex(-b - (delta**(1/2))) / (2 * a)

print("x1 = ", end="")
print(cmath.phase(x1))

print("x2 = ", end="")
print(cmath.phase(x2))
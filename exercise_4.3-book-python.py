A = float(input("Escreva o primeiro número: "))
B = float(input("Escreva o segundo número: "))
C = float(input("Escreva o terceiro número: "))

if A > B and A > C:
    print("O primeiro número é maior: %.2f" % A)
if A < B and A < C:
    print("O primeiro número é menor: %.2f" % A)
if B > A and B > C:
    print("O segundo número é maior: %.2f" % B)
if B < A and B < C:
    print("O segundo número é menor: %.2f" % B)
if C > A and C > B:
    print("O terceiro número é maior: %.2f" % C)
if C < A and C < B:
    print("O terceiro número é menor: %.2f" % C)
try:
    a = input("escreva um número:")
    b = input("escreva outro número:")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError): #captura divisão por zero e digitação de string
    print("Entrada inválida.")
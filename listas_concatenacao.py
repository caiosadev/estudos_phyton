L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2 #concatenação de listas
x = 0

while x < len(L3): #len é uma função que retorna o tamanho da lista, mesmo mudando o tamanho da lista.
    print(L3[x])
    x += 1
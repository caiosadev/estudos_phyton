motos = ["honda", "yamaha", "suzuki"]
print(motos)

#insere uma marca ao final da lista
motos.append("ducati")
print(motos)

#insere uma moto no índice 1
motos.insert(1, "kawazaki")
print(motos)

#mostra a última marca da lista, mas remove ela da lista
ultima_compra = motos.pop()
print(f"A última moto comprada foi uma {ultima_compra.title()}.")

#mostra a lista sem o último item pois foi removido pelo pop()
print(motos)

#insere o último item na lista novamente
motos.append(ultima_compra)
print(motos)
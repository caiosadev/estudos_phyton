cores = ["vermelho", "verde", "azul"]

existe = input("Busque uma cor: ")

if existe.lower() in cores: #lower() é uma função que transforma a string em minúscula, assim não importa se o usuário digitar a cor em maiúscula ou minúscula.
    print("A cor existe na lista.")
else:
    print("A cor não existe na lista.")
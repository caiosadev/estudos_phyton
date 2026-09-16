temp_fah = int(input("Qual a temperatura em Fahrenheit? "))
temp_cel = int(((temp_fah - 32) / 9) * 5)

print("A temperatura em Celsius é: %d graus." % temp_cel)
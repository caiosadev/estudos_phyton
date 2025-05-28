start_message = "Olá"

name_user = input("Qual o seu nome? ")
age_user = int(input("Qual a sua idade? "))
stature_user = float(input("Qual a sua altura? "))

print("%s, %s! Você têm %d anos e %1.2f de altura." % (start_message, name_user, age_user, stature_user))
deposito = float(input("Digite o depósito inicial: R$ "))
juros = float(input("Digite a taxa de juros (%): "))

saldo = deposito
total_juros = 0
mes = 1

while mes <= 24:
    rendimento = saldo * (juros / 100)
    saldo += rendimento
    total_juros += rendimento
    
    print("Mês %d: R$ %.2f" % (mes, saldo))

    mes += 1

print("Total ganho com juros: R$ %.2f" % total_juros)
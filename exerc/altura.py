
soma_altura = 0
quant_ent = 4

while quant_ent > 0:
    altura = input("Entre com a altura ")
    altura = float(altura)
    soma_altura += altura
    quant_ent -= 1

print(soma_altura)

#%%

Saldo_total = 0

while True:
    saldo = input("digite o saldo em conta: ")
    if saldo == "":
        break
    Saldo_total += float(saldo)

print(Saldo_total)


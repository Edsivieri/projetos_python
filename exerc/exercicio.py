while True:
    try:
        salario = float(input("digite seu salário: ").replace(",","."))
    except ValueError:
        print("Número digitado incorretamente ") 
        continue
    if salario < 0:
        print("Salario Negativo")
        continue
    break

    

while True:
    try:
        bonus = float(input("digite seu bonus: ").replace(",","."))
    except ValueError:
        print("Número digitado incorretamente ") 
        continue
    if bonus < 0:
        print("bonus Negativo")
        continue
    break


KPI = salario * bonus
print(f'Seu bonus será de {KPI:,.2f}')
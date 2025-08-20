# Isso é um comentário
while True:
    try:
        salario = float(input("digite seu salário: "))
        print(salario)
        break
    except ValueError:
        print("Número digitado incorretamente ") 
        continue

while True:
    try:
        bonus = float(input("digite seu bonus: "))
        print(bonus)
        break    
    except ValueError:
        print("Número digitado incorretamente ") 
        continue


KPI = salario + bonus


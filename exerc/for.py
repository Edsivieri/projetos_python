#%%

fizzbuzz = 0

for i in range(1,100+1):
    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

#%%

for i in range (1,100+1):
    if i % 7 == 0:
        print(i,"Bazz")
    if i % 5 == 0:
        print("buzz")
    if i % 3 == 0:
        print(i, "Fizz")
    else:
        print(i)
    #%%
for i in range(1, 106):
    rotulos = []                 # acumulador
    if i % 3 == 0:
        rotulos.append("Fizz")
    if i % 5 == 0:
        rotulos.append("Buzz")
    if i % 7 == 0:
        rotulos.append("Bazz")

    if rotulos:
        print(i, " ".join(rotulos))
    else:
        print(i)
# %%
##Escreva um programa que receba uma lista de 
# números do usuário e conte quantas vezes um número
#  específico aparece na lista. 
# Solicite ao usuário um número e exiba a contagem.

num = [1,2,3,3,2,1,1,1,1,1,5,6,7,7,6,5,42]

contador = 0
numerd = input("Digite um número: ")
numerd = int(numerd)


for i in num:
    if i  == numerd:
        contador += 1

print(contador)

#%%

#
#
#count = 1
#while count <=50:
    #print(f'a multipicação de {numero} por {count} é ', numero*count)
    #count += 1 
#
#
#print("fim")

numero = int(input("digite um número: "))

max_numero = int(input("digite um número: "))

for i in range(0, max_numero+1): 
    print(numero, "X", i, "=", numero*i)

print("fim")
#%%


def f(x):
    return 1 + x

f(10)

def juros_compostos(aporte: int, anos: int, taxa: float):
    """aaaabbb
    
    """
    return aporte * (1+taxa) ** anos
aporte = int(input("Digite seu aporte "))
taxa = float(input("Digite seu taxa "))
anos = int(input("Digite seu ano "))

juros_compostos(aporte, anos, taxa)


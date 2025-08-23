#%%
count = 1
while count <= 20:
    print(count)
    count = count +1
    
    

#%%
numero = int(input("digite um número: "))

count = 1
while count <=50:
    print(f'a multipicação de {numero} por {count} é ', numero*count)
    count += 1 


print("fim")
#%%
#quais numeros sao divisiveis por 4 no intervalo de 1 a 200

count = 4
while count <= 200:
    resto = count % 4
    if resto == 0:
        print(count)
    
    count += 1
    #%%

soma_altura = 0

quant_ent = 4

while quant_ent > 4:
    altura = input("Entre com a altura ")
    altura = float(altura)
    soma_altura += altura
    quant_ent -= 1

print(soma_altura)
#%%

numero = 12
max_numero = 100

for i in range(1, max_numero+1):
    print(numero, "X", i,"=", numero*i)

#%%

for i in range(16, 101):
    if i % 16== 0:
        print(i)
#%%
soma_altura = 0

for altura in range (1, 5):
    altura = input("digte uma altura")
    altura = float(altura)

    soma_altura += altura
    print(soma_altura)
    #%%
    edu = ["Edu", 30, False, "Solteiro", 8000.00]

    print(edu[1:10])
    
    edu.append("Ola")
    print(edu)

idades = [10, 20 ,30,670,50]

sum(idades)/len(idades)

#%%
numeros = [123, 435, 987, 1984, 2, 19, 423, -178, 320]
numeros.reverse()

print(numeros.index(min(numeros)))

numeros.index(max(numeros))

print(numeros)

#%%

fizzbuzz = 0

for i in range(0,100):
    if i% 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")


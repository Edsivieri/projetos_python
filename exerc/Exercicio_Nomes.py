while True:
    horario = input("Digite o horario atual no formato hhmm ").strip()
    if ':' not in horario:
        print("Formato Invalido, falta ':' ")
        continue

    hh_str, mm_str = horario.split(":",1)
    if not (hh_str.isdigit() and mm_str.isdigit()):
        print("Use apenas números para hora e minuto.")
        continue

    hh = int(hh_str)
    mm = int(mm_str)

    if not (0 < hh <= 23 and 0 < mm < 59):
        print("horário fora do intervalo ")
        continue

    print(f'São {hh} horas e {mm} minutos') 
    break
#%%
while True:
    nome = input("Digite seu nome: ").strip()
    
    partes = nome.split()

    if len(partes) <2:
        print("digite pelo menos nome e sobrenome")
        continue

    primeiro_nome = partes[0]
    segundo_nome = partes[1:-1]
    ultimo_nome = partes[-1]
    print(primeiro_nome, segundo_nome, ultimo_nome)
    break
# %%

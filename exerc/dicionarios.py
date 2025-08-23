## dicionarios são pares de chave valor = json  
###
# 
# 
# 
# 
# '''primeiro sempre a chave''''
#%%
a = {"Nome":"Edu", "Sobrenome":"Sivieri","idade":30, "formação":[1,2,3,4,5], "cargos":[
    {"nome":"Estagiario", "empresa":"Coelho e Gavioli"},{"nome":"Estagiario", "empresa":"Marmara"},
    {"nome":"Analista de Inteligencia", "empresa":"EREA"}]}

print(a["cargos"][-1]["nome"])
# %%


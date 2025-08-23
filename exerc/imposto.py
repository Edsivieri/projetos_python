#%%
def imposto(valor_produto: float, imposto_base: float, **kwargs):
    
    for i in kwargs:
        print(i, kwargs[i])
        imposto_base += valor_produto * kwargs[i]
    return imposto_base
    
    
    
#%%

impostos_gerais = {}
imposto(100, 0.20)


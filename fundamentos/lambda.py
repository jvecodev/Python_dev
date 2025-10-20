"""
    Lambda - funcoes anonimas 
    Função para potencia de números
"""

lista = [1,2,3,4,5,6]

"""
    Lambda acaba sendo redundante sendo que podemos usar 
    apenas o list comprehension

    lista2 = [ sla * 2 for sla in lista if sla > 0 ]
"""

lista2 = [ (lambda numero: numero * 2)(sla) for sla in lista if sla > 0 ]

print(lista2)


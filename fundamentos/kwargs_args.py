"""
    args -> são utilizados quando não temos certeza de 
    quantos argumentos queremos ter um uma função

"""

def sum (*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"soma total {sum_total}")

sum(4,5,6,7,8,9)


"""
    kwargs são parametros que podemos passar 
    a chave para respectivo argumento

    -Argumentos são passados como dicionario

"""

def presentation (**num):
    for chave, valor in num.items():
        print(f" {chave},  {valor}")

presentation(Num1 = 1, Num2 = 2, Num3 = 3)



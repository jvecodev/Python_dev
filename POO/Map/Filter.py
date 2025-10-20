numeros = [1, 2, 3, 4, 5]

# mantém apenas os ímpares
resultado = filter(lambda x: x % 2 != 0, numeros)

print(list(resultado))  

# nomes = ["Ana", "Bruno", "Carla"]

# for i, nome in enumerate(nomes):
#     print(i, nome)

# for i, nome in enumerate(nomes, start=1):
#     print(i, nome)


# """
#     Sem o enumarate usavamos o len(nomes)
# """

# for i in range(len(nomes)):
#     print(i, nomes[i])


alfabeto = "abcdefghijklmnopqrstuvwxyz"

sem_espaco = alfabeto.replace(" ", "")
letras_vetor = list(sem_espaco)

frase = "O Brasil é o país do futebol, o Brasil é penta."

for letra in sorted(
    [(i + 1, l) for i, l in enumerate(frase.replace(" ", "")) if l.lower() in alfabeto],
    key=lambda x: x[1].lower()
):
    print(letra[0], letra[1])

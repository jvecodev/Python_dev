
#Pipeline é um modelo de alto nível para tarefas de NLP
#Permite criar modelos pré-treinados com poucas linhas de código

from transformers import pipeline

gerador = pipeline("text-generation", model="pierreguillou/gpt2-small-portuguese")

texto = "Um transformer é um grande modelo de linguagem NLP"

resultado = gerador(texto, max_length=100, do_sample=True, top_k=50, top_p=0.95, num_return_sequences=3)

# Imprimindo os resultados
print("Texto original:", texto)
print("\nTextos gerados:")
for i, res in enumerate(resultado):
    print(f"{i+1}: {res['generated_text']}")
    print("-" * 50)
from transformers import pipeline

# Pipeline é um modelo de alto nível para tarefas de NLP

resumir = pipeline("summarization")


texto = ' A Revolução dos Cravos foi um movimento militar e popular que pôs fim à ditadura ' \
'do Estado Novo em Portugal, a 25 de abril de 1974. A revolução, liderada pelo Movimento das Forças Armadas (MFA), foi pacífica e ficou conhecida pelo ato dos soldados colocarem cravos nos canos das suas armas, um símbolo de esperança e liberdade. Este evento marcou o início da transição para um regime democrático, o fim do império colonial português e o restabelecimento das liberdades cívicas no país. '

resultado = resumir(texto, max_length=150, min_length=25, do_sample=True)

for i, res in enumerate(resultado):
    print(f"{i+1}: {res['summary_text']}")
    print("-" * 50)
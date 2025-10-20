from transformers import pipeline

mascarador = pipeline(
    "fill-mask", model="neuralmind/bert-base-portuguese-cased")

texto = "O melhor time do Brasil é o [MASK] e tambem "
resultado = mascarador(texto)

for i, res in enumerate(resultado):
    print(f"{i+1}: {res['sequence']} (score: {res['score']:.4f})")

    """
        exemplo de saída:
            1: O melhor time do Brasil é o Flamengo (score: 0.1374)
            2: O melhor time do Brasil é o Corinthians (score: 0.1056)
            3: O melhor time do Brasil é o Botafogo (score: 0.0991)
            4: O melhor time do Brasil é o Palmeiras (score: 0.0969)
            5: O melhor time do Brasil é o Fluminense (score: 0.0794)
    """

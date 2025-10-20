import google.generativeai as genai
import os

# Para o seu teste:
genai.configure(api_key="AIzaSyBysLlRFoGVs_6OfONPdg0kWLtKJRqB1tY")

# O modelo ideal para começar a estudar sem faturamento
model = genai.GenerativeModel("gemini-1.5-flash-latest")

prompt = "Cite uma frase de Confucio, o melhor filósofo chinês."
resposta = model.generate_content(prompt)

print(resposta.text)
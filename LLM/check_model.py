import google.generativeai as genai

# Coloque a sua chave aqui ou use variáveis de ambiente
genai.configure(api_key="AIzaSyBysLlRFoGVs_6OfONPdg0kWLtKJRqB1tY")

print("Modelos disponíveis que suportam 'generateContent':")
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
from google import genai

# Coloque sua NOVA chave aqui dentro das aspas
GOOGLE_API_KEY = "AIzaSyCxJPMkxY64mQPnREzHEOZxSU9I07XAIlA"

# O novo padrão usa um "Client" para fazer a conexão
client = genai.Client(api_key=GOOGLE_API_KEY)

print("Tentando contato com o servidor novo...")

# Fazendo a requisição usando a nova estrutura
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Responda apenas com a seguinte frase: A conexão com a API foi estabelecida com sucesso!'
)

print("Resposta da IA:")
print(response.text)
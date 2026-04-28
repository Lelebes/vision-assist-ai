import keyboard
from PIL import ImageGrab, Image
from google import genai
import pyttsx3
import time
# CONFIGURAÇÕES INICIAIS

# 1. Configuração da IA
GOOGLE_API_KEY = "SUA_CHAVE_AQUI"
client = genai.Client(api_key=GOOGLE_API_KEY)

# 2. Configuração da Voz
motor_voz = pyttsx3.init()
motor_voz.setProperty('rate', 170) # Velocidade da voz (pode ajustar depois)

# Lógica Principal
def executar_leitor_acessibilidade():
    print("\nAtalho detectado! Iniciando processo...")
    
    # Capturar a tela
    caminho_imagem = "tela_temporaria.png"
    imagem = ImageGrab.grab()
    imagem.save(caminho_imagem)
    print("Tela capturada. Analisando imagem...")

    # O Comando para a IA
    prompt = """
    Você é um assistente de acessibilidade para uma pessoa com deficiência visual. 
    Descreva o que está nesta tela de forma direta, clara e resumida. 
    Foque apenas no conteúdo principal, textos importantes e botões de ação. 
    Ignore cores, logotipos e elementos puramente decorativos. 
    Seja breve, pois o texto será lido em voz alta.
    """

    # Enviar para o Gemini
    img_para_ler = Image.open(caminho_imagem)
    tentativas = 0
    max_tentativas = 2
    sucesso = False

    while tentativas < max_tentativas and not sucesso:
        try:
            # Na primeira tentativa, usa o modelo mais robusto. Na segunda, o mais leve.
            modelo_atual = 'gemini-2.5-flash' if tentativas == 0 else 'gemini-1.5-flash'
            print(f"Conectando ao servidor (Modelo: {modelo_atual})...")
            
            response = client.models.generate_content(
                model=modelo_atual,
                contents=[prompt, img_para_ler]
            )
            
            texto_gerado = response.text
            print("\n[RESPOSTA DA IA]:")
            print(texto_gerado)
            
            print("\n[INFO] Lendo o texto em voz alta...")
            motor_voz.say(texto_gerado)
            motor_voz.runAndWait()
            print("[INFO] Leitura concluída. Aguardando novo comando...")
            
            sucesso = True # Sai do loop se deu certo

        except Exception as erro:
            mensagem_erro = str(erro)
            tentativas += 1
            
            # Se for erro 503 (Servidor Lotado) e ainda tiver tentativas
            if "503" in mensagem_erro and tentativas < max_tentativas:
                print("[AVISO] Servidor do Google sobrecarregado. Aguardando 5 segundos para tentar o Plano B...")
                time.sleep(5)
            else:
                # Se for outro erro ou acabarem as tentativas, mensagem de erro.
                print(f"\n[ERRO CRÍTICO] Falha irreversível: {mensagem_erro}")
                motor_voz.say("O servidor está indisponível no momento. Tente novamente mais tarde.")
                motor_voz.runAndWait()
                break # Quebra o loop

# Fica rodando em segundo plano

print("=== Leitor de Tela com IA Ativo ===")
print("Pressione 'ctrl + alt + space' em qualquer lugar do PC para ler a tela.")
print("Pressione 'esc' para fechar o programa.")

keyboard.add_hotkey('ctrl+alt+space', executar_leitor_acessibilidade)
keyboard.wait('esc')
print("Sistema encerrado.")
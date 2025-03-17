import google.generativeai as genai
from dotenv import load_dotenv

# Configuração da API
load_dotenv()
genai.configure(api_key=os.getenv("Gemini_api_key"))#chave api está guardada em um arquivo .env por segurança

# Lista para armazenar o histórico da conversa
historico_conversa = []

def enviar_mensagem(mensagem):
    """Envia uma mensagem para o modelo Gemini AI e mantém o histórico."""
    try:
        modelo = genai.GenerativeModel("gemini-1.5-pro")

        # Adiciona a mensagem do usuário ao histórico
        historico_conversa.append({"role": "user", "parts": [mensagem]})

        # Envia todas as mensagens acumuladas para manter o contexto
        resposta = modelo.generate_content(historico_conversa)

        # Adiciona a resposta ao histórico
        historico_conversa.append({"role": "model", "parts": [resposta.text]})

        return resposta.text  

    except Exception as e:
        return f"⚠️ Erro: {str(e)}"

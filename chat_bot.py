import google.generativeai as genai

genai.configure(api_key="AIzaSyAIXvjpN9sCcya9upzO-jWb0s26rq2pIpA")

# Lista para armazenar o histórico da conversa
historico_conversa = []

def enviar_mensagem(mensagem):
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
        return f"Erro ao processar a mensagem: {str(e)}"








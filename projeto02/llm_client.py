from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY não encontrada")

client = OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1"
)

def gerar_resposta(prompt, temperature=0.2):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=temperature,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("Erro na API:", e)
        return None
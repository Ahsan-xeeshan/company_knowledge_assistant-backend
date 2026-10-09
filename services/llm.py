import os

from dotenv import load_dotenv

from openai import OpenAI


load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "openai/gpt-4o-mini"
)

def generate_answer(
        question:str,
        context:str
):
    prompt = f"""
You are a company knowledge assistant.

Answer the user's question using ONLY the
provided company context.

Do not use outside knowledge.

Do not invent or assume information.

If the answer is not available in the context,
say:

"I don't have enough information in the
available company documents to answer that."

Keep the answer concise and clear.

Company Context:
{context}

User Question:
{question}

"""


    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        temperature=0 
    )
    return response.choices[0].message.content
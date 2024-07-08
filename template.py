from openai import AzureOpenAI
from setup import get_keys_secure

client, model = get_keys_secure()

response = client.chat.completions.create(
    model = model,
    messages=[
        {
            "role": "system",
            "content": [
                {"type": "text", "text": "You are a helpful bot that can answer questions."}
            ]
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What is the capital of Czech Republic?"}
            ]
        }
    ]
)

print(response.choices[0].message.content)
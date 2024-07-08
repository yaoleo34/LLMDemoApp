import os
from openai import AzureOpenAI
import base64
from setup import get_keys_secure

def read_file(file):
    with open(file, 'r') as f:
        return f.read()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def get_llm_responses(system, question, image = None, history = []):
    client, deployment = get_keys_secure()
    if image is not None:
        history.append({
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {"type": "image_url", "image_url": {
                            "url": f"data:image/png;base64,{image}"}
                    }
                ]
            })
    else:
        history.append({
                "role": "user",
                "content": question
        })

    system_prompt = {
        "role": "system",
        "content": [
            {"type": "text", "text": system}
        ]
    }

    completion = client.chat.completions.create(
        model=deployment,
        messages= [system_prompt] + history
    )
    response = completion.choices[0].message.content

    history.append({
            "role": "assistant",
            "content": response
    })
    return (response, history)



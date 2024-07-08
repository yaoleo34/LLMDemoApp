
import os
from openai import AzureOpenAI
import base64
from setup import get_keys_secure
from llm_app import get_llm_responses, encode_image, read_file

client, deployment = get_keys_secure()

def eval_response(answer, system, prompt, image = None): 
    system_prompt = read_file("eval_system.txt")
    eval_system_prompt = {
        "role": "system",
        "content": [
            {"type": "text", "text": system_prompt}
        ]
    }

    question = f"system_message: {system}\nuser_message: {prompt}\nllm_response: {answer}"
    user_prompt = {
        "role": "user",
        "content": [
            {"type": "text", "text": question},
            {"type": "image_url", "image_url": {
                    "url": f"data:image/png;base64,{image}"}
            }
        ]

    }

    completion = client.chat.completions.create(
        model=deployment,
        temperature=0,
        messages= [eval_system_prompt, user_prompt]
    )
    response = completion.choices[0].message.content
    return response


#answer = read_file("response_v1.txt")
answer = "The provided image does not have enough context to answer the question."
image = encode_image("image1.png")
system = read_file("system_v2.txt")
prompt = read_file("question_intelliJ.txt")
#answer = get_llm_responses(system, prompt, image)
result = eval_response(answer, system, prompt, image)
print(result)
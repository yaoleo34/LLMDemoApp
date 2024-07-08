from llm_app import encode_image, read_file, get_llm_responses

IMAGE_PATH = "image1.png"
base64_image = encode_image(IMAGE_PATH)

system = read_file("system_v2.txt")
question = read_file("question_intelliJ.txt")

response, history = get_llm_responses(system, question, base64_image)

print(response)

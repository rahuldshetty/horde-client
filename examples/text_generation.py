from horde_client import HordeClient, ModelType, TextGenParams

client = HordeClient()

# List available models
print("===== Model List =====")
for model in client.list_models(type=ModelType.text)[:5]:
    print(model)

# Text Generation
prompt =  """### Instruction: 
Tell me a knock knock joke.

### Response:
"""

print("\n===== Prompt =====")
print(prompt)

params = TextGenParams(
    max_context_length = 512,
    temperature=0.8
)

text_gen_ouput = client.text_gen(prompt, params=params)

print("\n===== Output =====")
print(text_gen_ouput)
print(text_gen_ouput.generations[0].text)

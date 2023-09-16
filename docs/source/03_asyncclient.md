# Async Horde Client



```python
import asyncio

from horde_client import AsyncHordeClient, ModelType, TextGenParams

client = AsyncHordeClient(
    insecure=True
)

prompt =  """### Instruction: 
Tell me a knock knock joke.

### Response:
"""

# Text Generation
async def main():
    # List available models
    print("===== Model List =====")
    models = await client.list_models(type=ModelType.text)
    for model in models[:5]:
        print(model)

    # Text Generation
    print("\n===== Prompt =====")
    print(prompt)

    params = TextGenParams(
        max_context_length = 512,
        temperature=0.8
    )

    text_gen_ouput = await client.text_gen(prompt, params=params)

    print("\n===== Output =====")
    print(text_gen_ouput)
    print(text_gen_ouput.generations[0].text)


asyncio.get_event_loop().run_until_complete(main())
```
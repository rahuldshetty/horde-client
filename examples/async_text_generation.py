import asyncio

from horde_client import AsyncHordeClient, ModelType

client = AsyncHordeClient()


# Text Generation
async def main():
    # List available models
    print("===== Model List =====")
    models = await client.list_models(type=ModelType.text)
    for model in models[:5]:
        print(model)

asyncio.get_event_loop().run_until_complete(main())
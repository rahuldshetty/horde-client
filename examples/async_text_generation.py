import asyncio

from horde_client import AsyncHordeClient, ModelType

client = AsyncHordeClient()


# Text Generation
async def main():
    # List available models
    print("===== Model List =====")
    for model in await client.list_models(type=ModelType.text)[:5]:
        print(model)

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
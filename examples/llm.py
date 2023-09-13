from horde_client import HordeClient 

client = HordeClient()

# List available models
for model in client.list_models():
    print(model)



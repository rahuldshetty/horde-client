# Image Generation

```python
import io, base64
from PIL import Image

from horde_client import HordeClient, ModelType, ImageGenParams

client = HordeClient(
    # To access public KoboldAI service
    insecure=True 
)

# List available models
print("===== Model List =====")
for model in client.list_models(type=ModelType.text)[:20]:
    print(model)

# Set model
client.clear_model()
client.set_model('stable_diffusion')

# Image Generation Prompt
prompt =  """an orange cat, wearing black suit, reading newspaper, in bench, park, outdoors"""

print("\n===== Prompt =====")
print(prompt)

params = ImageGenParams()

image_gen_ouput = client.image_gen(prompt, params=params)

print("\n===== Output =====")
file_output = "my-cat.png"
img = Image.open(io.BytesIO(base64.decodebytes(bytes(image_gen_ouput.generations[0].img, "utf-8"))))
img.save(file_output)
print('Output saved to ' + file_output)
```

![my-cat.png](_static/my-cat.jpeg)
# Quickstart

Install Horde Client from [PyPI](https://pypi.org/project/horde-client/): 

`pip install horde-client`

Sample Code:

```python
from horde_client import HordeClient, TextGenParams

# Initialize Client
client = HordeClient(
  # To access public KoboldAI service
  insecure=True
)

# Prompt
prompt =  """### Instruction: 
Tell me a knock knock joke.

### Response:
"""

# Setup Text Generation Parameters
params = TextGenParams(
    max_context_length = 512,
    temperature=0.8
)

# Run Generation (Sync)
text_gen_ouput = client.text_gen(prompt, params=params)

print(text_gen_ouput.generations[0].text)
# Knock knock!
# Who's there?
# Interrupting cow.
# Interrupting cow who?
# Mooooooo!
```
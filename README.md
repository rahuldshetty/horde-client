

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/rahuldshetty/horde-client">
    <img src="https://raw.githubusercontent.com/rahuldshetty/horde-client/master/images/logo.png" alt="Logo" width="140" height="130">
  </a>

  <!-- <h3 align="center">Horde Client</h3> -->

  <p align="center">
    <a href="https://github.com/badges/shields/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/contributors/rahuldshetty/horde-client" /></a>
    <a href="https://github.com/badges/shields/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/rahuldshetty/horde-client" /></a>
    <a href='https://horde-client.readthedocs.io/en/latest/?badge=latest'>
      <img src='https://readthedocs.org/projects/horde-client/badge/?version=latest' alt='Documentation Status' />
    </a>
  </p>

  <p align="center">
    Easy-to-use Python Interface for KoboldAI Horde.
    <!-- <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br /> -->
    <br />
    <!-- <a href="#">View Demo</a> -->
    <!-- · -->
    <a href="https://github.com/rahuldshetty/horde-client/issues">Report Bug</a>
    ·
    <a href="https://github.com/rahuldshetty/horde-client/issues">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This project provides Python Client to interact with [KoboldAI Horde](https://horde.koboldai.net) service, which is a crowdsourced distributed cluster program that offers Image generation and Text Generation workers. Through this utility package, you can leverage these services from your application. 

* Simple & Easy-to-use
* Support for Text & Image Generation
* LangChain Integration 
* Asynchronous Client

> Note: There is an official Python SDK under development from Haidra-org: https://github.com/Haidra-Org/horde-sdk.

> Security Note: Do NOT send any private information while connecting to the public KoboldAI service. There is no control on how the data is processed. However, if you have private & secured KoboldAI Endpoints then feel free to experiment yourself. 

<!-- Installation -->
## Quickstart

Install Horde Client with pip: 

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

<!-- ROADMAP -->
## Roadmap

- [X] Text Generation Support
- [ ] LangChain/LlaMaIndex Integration
- [X] Image Generation Support
- [X] Asynchronous Client
- [X] Readthedocs integration
- [ ] Tests

Missing Something? Raise a [request](https://github.com/rahuldshetty/horde-client/issues) 

<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


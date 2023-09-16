# LangChain

If you have worked with LLMs the you must have definitely come across [LangChain](https://python.langchain.com/docs/get_started/introduction). LangChain is a framework that provides off-the-shelf modules for building "Chains" (Pipelines) using AI & Data systems. 

You can think of it as a LEGO blocks where you combine different colored or type of blocks to build the final product.

We are introducing a new *LangChain* compatible LLM module for Horde-Client. With this LLMClient you can easily integrate Horde-Client with your new or existing LangChain pipeline.

## Example

```python
from horde_client import HordeClientLLM, TextGenParams

from langchain import LLMChain
from langchain.prompts import PromptTemplate

# Prepare HordeClientLLM
params = TextGenParams(
    max_context_length=256,
    max_length=64,
    temperature=0.8
)

llm = HordeClientLLM(
    # To access public Horde Client
    insecure=True,

    # TextGen Parameters for HordeAI Client
    params=params
)

# Prompt Template
template = """### Instruction:
Create a fancy company name for a company that makes {product}.
### Response:
"""

prompt= PromptTemplate(input_variables=["product"], template=template)

# Chain Prompt with LLM
chain = LLMChain(
    llm = llm,
    prompt = prompt
)

print(chain.run("colorful socks"))
# "Socktopia"

print(chain.run("mobiles"))
# "Elysium Technologies Inc."
```

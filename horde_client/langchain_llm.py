from horde_client import config
from horde_client.model import TextGenParams
from horde_client.client import HordeClient
from horde_client.async_client import AsyncHordeClient


from typing import Any, List, Mapping, Optional

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM

class HordeClientLLM(LLM):
    base_url: str = config.API_BASE_URL
    """Base URL for KoboldAI Horde Service"""

    api_token: str = config.ANON_KEY
    """API Token for KoboldAI Horde Service"""
    
    insecure: bool = False
    """Flag controls access to public Horde service."""
    
    params: TextGenParams = TextGenParams()
    """Text Generation Parameter"""
    
    models: List[str] = []
    """Models to accept request."""

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        text = self.text_generate(prompt)

        if stop is not None:
            for sequence in stop:
                if text.endswith(sequence):
                    text = text[: -len(sequence)].rstrip()

        return text

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {
            "base_url": self.base_url,
            "api_token": self.api_token,
            "insecure": self.insecure,
            "params": self.params,
            "models": self.models
        }

    def text_generate(self, prompt):
        '''
        Synchronous Text Generation
        '''
        client = HordeClient(
            self.base_url,
            self.api_token,
            self.insecure
        )
        
        for model in self.models:
            client.set_model(model)
        
        return client.text_gen(
            prompt,
            self.params
        ).generations[0].text
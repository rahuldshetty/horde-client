import requests, random, time
from urllib.parse import  urljoin
from typing import List

from horde_client import config
from horde_client import model

class HordeClient:
    def __init__(self, 
            base_url=config.API_BASE_URL,
            api_token=config.ANON_KEY
        ):
        '''
        Instantiate HordeClient SDK.

        Parameters:
        -----------
        base_url (str): Kobold Horde API URL (Default: https://horde.koboldai.net/api/)
        api_token (str): Kobold Horde API Key (Default: 0000000000)
        '''
        self.__base_url = base_url
        self.__api_token = api_token
        self.__models = []
    
    def __headers(self):
        return {
            'Apikey': self.__api_token,
            'User-Agent': random.choice(config.user_agents)
        }

    def get(self, endpoint, path_params:dict = None, query_params:dict = None):
        '''
        Get Request Endgine
        '''
        endpoint = endpoint
        
        # Format path parameter in endpoint url 
        if path_params:
            endpoint = endpoint.format(
                **path_params
            )
        
        url = urljoin(self.__base_url, endpoint)

        # Additional Header tokens added here
        headers = self.__headers()

        response = requests.get(
            url,
            params = query_params,
            headers=headers
        )

        return response.json()

    def post(self, endpoint, path_params:dict = None, query_params:dict = None, json_payload:dict = {}):
        '''
        Post Request Endgine
        '''
        endpoint = endpoint
        
        # Format path parameter in endpoint url 
        if path_params:
            endpoint = endpoint.format(
                **path_params
            )
        
        url = urljoin(self.__base_url, endpoint)

        # Additional Header tokens added here
        headers = self.__headers()
        
        response = requests.post(
            url,
            params = query_params,
            headers=headers,
            json=json_payload
        )

        return response.json()


    def list_models(self, type:model.ModelType) -> List[model.Model]:
        results = self.get(
           config.ENDPOINT_LIST['V2__MODEL_LIST'], 
            query_params={
                'type': type.value
            }
        )
        model_list = []
        for model_obj in results:
            model_list.append(
                model.Model(**model_obj)
            )
        return model_list
    
    def clear_model(self):
        self.__models = []

    def set_model(self, model:str):
        self.__models.append(model)
    
    def check_job_status(self, job:model.Job) -> model.JobResponse:
        status = self.get(
            config.ENDPOINT_LIST['V2__ASYNC_TEXT_STATUS'],
            path_params={
                'id': job.id
            }
        )
        return model.JobResponse(**status)

    def text_gen(self, prompt:str, params:model.TextGenParams = model.TextGenParams()):
        request_data = model.TextGenRequest(
            models = self.__models,
            params = params,
            prompt = prompt
        )

        job_result = self.post(
            config.ENDPOINT_LIST['V2__ASYNC_TEXT_SUBMIT'],
            json_payload = request_data.model_dump()
        )

        job = model.Job(
            **job_result
        )

        while True:
            job_status = self.check_job_status(job)
            if job_status.done or not job_status.is_possible:
                return job_status
            time.sleep(config.REQUEST_RETRY_TIMEOUT)
        

        

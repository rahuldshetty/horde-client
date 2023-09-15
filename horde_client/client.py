import requests, random, time
from urllib.parse import  urljoin
from typing import List

from horde_client import config
from horde_client import model
from horde_client import errors

class HordeClient:
    def __init__(self, 
            base_url:str = config.API_BASE_URL,
            api_token:str = config.ANON_KEY,
            insecure:bool = False
        ):
        '''
        Instantiate HordeClient SDK.

        Parameters:
        -----------
        base_url (str):  KoboldAI API URL (Default: https://horde.koboldai.net/api/)
        api_token (str): KoboldAI API Key (Default: 0000000000)
        insecure (bool): Enabling insecure mode allows access to public KoboldAI. 
                         You will need to provide base_url when this flag is off (Default False)
        '''
        self.__base_url = base_url.strip()
        self.__api_token = api_token.strip()
        self.__insecure = insecure
        self.__models = []

        self.validate_insecure_permission()
    

    def validate_insecure_permission(self):
        '''
        To avoid accidental data leaks to public KoboldAI services, users have to manually enabled insecure mode.
        This methods is called during class initialization to validate the checks.
        '''
        if self.__insecure == False and self.__base_url == config.API_BASE_URL:
            raise errors.InsecureModePermissionError()
    
    def __headers(self):
        '''
        '''
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
        '''
        '''
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
        '''
        '''
        self.__models = []

    def set_model(self, model:str):
        '''
        '''
        self.__models.append(model)
    
    def check_job_status(self, job:model.Job) -> model.JobResponse:
        '''
        '''
        status = self.get(
            config.ENDPOINT_LIST['V2__ASYNC_TEXT_STATUS'],
            path_params={
                'id': job.id
            }
        )
        return model.JobResponse(**status)

    def text_gen(self, prompt:str, params:model.TextGenParams = model.TextGenParams()):
        '''
        '''
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
        

        

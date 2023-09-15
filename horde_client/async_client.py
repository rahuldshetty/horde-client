import random, time, json
from urllib.parse import  urljoin
from typing import List

import asyncio
from asyncio_requests.asyncio_request import request

from horde_client import config
from horde_client import model
from horde_client import errors

class AsyncHordeClient:
    def __init__(self, 
            base_url:str = config.API_BASE_URL,
            api_token:str = config.ANON_KEY,
            insecure:bool = False
        ):
        '''
        Instantiate Async HordeClient SDK.

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
    
    def __gen_query_params_string(self, query_params: dict):
        if not query_params: return ""
        return "?" + "&".join([ k + "=" + v for k, v in  query_params.items()])

    async def get(self, endpoint, path_params:dict = None, query_params:dict = None):
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
        
        # Concatenate Qury Params
        url += self.__gen_query_params_string(query_params)

        response = await request(
            url,
            protocol = 'HTTPS',
            protocol_info={
                "request_type": "GET",
                "headers": headers
            }
        )

        # TODO: Handle Exceptions

        result = response['api_response']

        if 200 <= result['status_code'] < 300 :
            return result['json']

    async def post(self, endpoint, path_params:dict = None, query_params:dict = None, json_payload:dict = {}):
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
        
        # Concatenate Qury Params
        url += self.__gen_query_params_string(query_params)

        response = await request(
            url,
            data=json_payload,
            protocol = 'HTTPS',
            protocol_info={
                "request_type": "POST",
                "headers": headers
            }
        )

        # TODO: Handle Exceptions
        result = response['api_response']

        if 200 <= result['status_code'] < 300 :
            return result['json']


    async def list_models(self, type:model.ModelType) -> List[model.Model]:
        '''
        '''
        results = await self.get(
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
    
    async def check_job_status(self, job:model.Job) -> model.JobResponse:
        '''
        '''
        status = await self.get(
            config.ENDPOINT_LIST['V2__ASYNC_TEXT_STATUS'],
            path_params={
                'id': job.id
            }
        )
        return model.JobResponse(**status)

    async def text_gen(self, prompt:str, params:model.TextGenParams = model.TextGenParams()):
        '''
        '''
        request_data = model.TextGenRequest(
            models = self.__models,
            params = params,
            prompt = prompt
        )

        job_result = await self.post(
            config.ENDPOINT_LIST['V2__ASYNC_TEXT_SUBMIT'],
            json_payload = request_data.model_dump()
        )

        job = model.Job(
            **job_result
        )

        while True:
            job_status = await self.check_job_status(job)
            if job_status.done or not job_status.is_possible:
                return job_status
            await asyncio.sleep(config.REQUEST_RETRY_TIMEOUT)
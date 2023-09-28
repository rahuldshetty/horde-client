API_BASE_URL = "https://horde.koboldai.net/api/"
ANON_KEY = '0000000000'
REQUEST_RETRY_TIMEOUT = 12

ENDPOINT_LIST = {
    "V2__MODEL_LIST": "v2/status/models",
    "V2__ASYNC_TEXT_SUBMIT": "v2/generate/text/async",
    "V2__ASYNC_TEXT_STATUS": "v2/generate/text/status/{id}",

    "V2__ASYNC_IMAGE_SUBMIT": "v2/generate/async",
    "V2__ASYNC_IMAGE_PROGRESS_STATUS": "v2/generate/check/{id}",
    "V2__ASYNC_IMAGE_STATUS": "v2/generate/status/{id}",
}

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
]



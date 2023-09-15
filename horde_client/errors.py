from horde_client import config

class HordeClientException(Exception):
    pass

class InsecureModePermissionError(HordeClientException):
    def __init__(self, message="Due to security reasons, direct access to public KoboldAI services has been disabled. Enable `insecure` mode in the client settings to access the service."):
        super().__init__(message)

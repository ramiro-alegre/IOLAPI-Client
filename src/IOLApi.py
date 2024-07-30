from datetime import datetime
from response_api.token.token import Token
from response_api.mi_cuenta.estado_cuenta import EstadoCuenta
from response_api.mi_cuenta.portafolio import Portafolio
from response_api.mi_cuenta.operaciones import Operaciones, Operacion
from utils import http_utils, iol_api_utils
from exceptions.token_expired_error import TokenExpiredError
import json

class IOLApi():
    """
    IOL API Class \n
    Repo: https://github.com/ramiro-alegre/IOLAPI-Client
    """
    _IOL_BASE_URL = 'https://api.invertironline.com/'
    _IOL_API_VERSION = 'v2/'
    _IOL_API_BASE_URL = f'{_IOL_BASE_URL}api/{_IOL_API_VERSION}'
    
    token_jwt : str
    token_jwt_expires_in : datetime
    refresh_token : str
    refresh_token_expires_in : datetime
    
    def __init__(self):
        pass
    
    async def login_async(self, username:str, password:str) -> Token:
        """Primer método a llamar antes de realizar cualquier acción

        Args:
            username (str): Usuario (Correo electronico de la cuenta)
            password (str): Contraseña (Contraseña de la cuenta)
        """
        data = {
            'username': username,
            'password': password,
            'grant_type': 'password'
        }
        response = await http_utils.post_util(f'{self._IOL_BASE_URL}token', body=data)
        token = Token.from_dict(response)
        IOLApi.token_jwt = token.access_token
        IOLApi.token_jwt_expires_in = iol_api_utils.parse_http_date(http_date=token.expires)
        IOLApi.refresh_token = token.refresh_token
        IOLApi.refresh_token_expires_in = iol_api_utils.parse_http_date(http_date=token.refreshexpires)
        
        return token

    async def check_token_jwt_async(self) -> None:
        now = datetime.now()
        if IOLApi.token_jwt_expires_in > now:
            return
        if IOLApi.refresh_token_expires_in < now:
            raise TokenExpiredError('Es necesario hacer login otra vez')
        
        data = {
            'refresh_token': IOLApi.refresh_token,
            'grant_type': 'refresh_token'
        }
        response = await http_utils.post_util(url=f'{self._IOL_BASE_URL}token', body=data)
        responseDict : dict = json.loads(response.text)
        token = Token.from_dict(responseDict)

        IOLApi.token_jwt = token.access_token
        IOLApi.token_jwt_expires_in = iol_api_utils.parse_http_date(http_date=token.expires)
        IOLApi.refresh_token = token.refresh_token
        IOLApi.refresh_token_expires_in = iol_api_utils.parse_http_date(http_date=token.expires_in)
    
    async def get_estadocuenta_async(self) -> EstadoCuenta:
        await self.check_token_jwt_async()
        data = await http_utils.get_util(
            url= f'{self._IOL_API_BASE_URL}estadocuenta',
            headers= self.__get_authorization_header()
        )
        return EstadoCuenta.from_dict(data)

    async def get_portafolio_by_pais_async(self, pais:str = 'argentina') -> Portafolio:
        """Permite obtener los activos que tengo en mí cuenta. Por ejemplo, cedears.

        Args:
            pais (str, optional): 'argentina' o 'estados_Unidos'

        Returns:
            Portafolio
        """
        await self.check_token_jwt_async()
        data = await http_utils.get_util(
            url= f'{self._IOL_API_BASE_URL}portafolio/{pais}',
            headers= self.__get_authorization_header()
        )
        return Portafolio.from_dict(data)
    
    async def get_operaciones_async(self, numero : int) -> dict:
        await self.check_token_jwt_async()
        data = await http_utils.delete_util(
            url= f'{self._IOL_API_BASE_URL}operaciones/{numero}',
            headers= self.__get_authorization_header()
        )
        return data
    
    async def get_operaciones_async(self) -> Operaciones:
        await self.check_token_jwt_async()
        data = await http_utils.get_util(
            url= f'{self._IOL_API_BASE_URL}operaciones',
            headers= self.__get_authorization_header()
        )
        return Operaciones.from_dict(data)
    
    def __get_authorization_header(self) -> dict:
        return {"Authorization": f"Bearer {IOLApi.token_jwt}"}
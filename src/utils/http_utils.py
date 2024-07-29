import aiohttp

async def get_util(url:str, headers:dict) -> dict:
    """Lanza una petición GET asincrona
    """
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=url) as response:
            return await response.json()

async def post_util(url:str, body, headers:dict = None) -> dict:
    """Lanza una petición POST asincrona
    """
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url=url,data=body) as response:
            return await response.json()
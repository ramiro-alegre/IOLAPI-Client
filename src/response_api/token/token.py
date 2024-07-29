from typing import Any
from dataclasses import dataclass

@dataclass
class Token:
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    issued: str
    expires: str
    refreshexpires: str
    
    @staticmethod
    def from_dict(obj: Any) -> 'Token':
        _access_token = str(obj.get("access_token"))
        _token_type = str(obj.get("token_type"))
        _expires_in = int(obj.get("expires_in"))
        _refresh_token = str(obj.get("refresh_token"))
        _issued = str(obj.get(".issued"))
        _expires = str(obj.get(".expires"))
        _refreshexpires = str(obj.get(".refreshexpires"))
        return Token(_access_token, _token_type, _expires_in, _refresh_token, _issued, _expires, _refreshexpires)
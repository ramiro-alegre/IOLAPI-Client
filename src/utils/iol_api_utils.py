from datetime import datetime

def parse_http_date(http_date:str) -> datetime:
    return datetime.strptime(http_date, '%a, %d %b %Y %H:%M:%S %Z')
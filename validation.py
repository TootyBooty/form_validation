import re 
from typing import Literal, Dict


# регулярные выражения для валидации полей
date_pattern = r'^(^(0?[1-9]|[12][0-9]|3[01])(\.)(0?[1-9]|1[012])(\.)\d{4}$)|(^\d{4}(\-)(0?[1-9]|1[012])(\-)(0?[1-9]|[12][0-9]|3[01])$)$'
phone_pattern = r'^(\+7){1}( ){1}[0-9]{3}( ){1}[0-9]{3}( ){1}[0-9]{2}( ){1}[0-9]{2}$'
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


async def field_validate(field:str) -> Literal['date', 'phone', 'email', 'text']:
    if re.search(date_pattern, field): return 'date'
    elif re.search(phone_pattern, field): return 'phone'
    elif re.search(email_pattern, field): return 'email'
    else: return 'text'

async def validate_dict_values(d:Dict[str, str]) -> Dict[str, str]:
    for k, v in d.items():
        d[k] = await field_validate(v)
    return d
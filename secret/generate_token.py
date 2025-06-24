from datetime import datetime, timedelta, timezone
import os
import jwt
from dotenv import load_dotenv


load_dotenv()
CONNECT_SECRET = os.getenv('CONNECT_SECRET')
if not CONNECT_SECRET:
    raise ValueError('CONNECT_SECRET is not set')


JWT_ALGORITHM = 'HS256'
widgetId = ''

now = datetime.now(timezone.utc)
payload = {
'sub': widgetId, # don't add single quotes, such as 'widgetId'
'iat': now,
'exp': now + timedelta(days=365),
'token_user': 'usak'
}

header = {
'typ': "JWT",
'alg': 'HS256'
}

encoded_token = jwt.encode((payload), CONNECT_SECRET, algorithm=JWT_ALGORITHM, headers=header)

print(encoded_token)
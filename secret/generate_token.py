from datetime import datetime, timedelta, timezone
import os
import jwt
from dotenv import load_dotenv


load_dotenv()
CONNECT_SECRET = os.getenv('CONNECT_SECRET')
if not CONNECT_SECRET:
    raise ValueError('CONNECT_SECRET is not set')

WIDGET_ID= os.getenv('WIDGET_ID')
if not WIDGET_ID:
    raise ValueError('WIDGET_ID is not set')


JWT_ALGORITHM = 'HS256'

now = datetime.now(timezone.utc)
payload = {
'sub': WIDGET_ID, # don't add single quotes, such as 'widgetId'
'iat': now,
'exp': now + timedelta(hours=24),
'segmentAttributes': {"connect:Subtype": {"ValueString" : "connect:Guide"}}, 
'attributes': {"name": "Jane", "memberID": "123456789", "email": "Jane@example.com", "isPremiumUser": "true", "age": "45"}
}

header = {
'typ': "JWT",
'alg': JWT_ALGORITHM
}

encoded_token = jwt.encode((payload), CONNECT_SECRET, algorithm=JWT_ALGORITHM, headers=header)

print(encoded_token)
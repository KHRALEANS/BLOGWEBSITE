import jwt
import datetime
import time
import settings

username = 'rabbit'

encoded_jwt = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=10)}, settings.JwtKey, algorithm="HS256")
print(encoded_jwt)

decoded = jwt.decode(encoded_jwt, settings.JwtKey, algorithms=["HS256"])
print(decoded)

time.sleep(15)

decoded = jwt.decode(encoded_jwt, settings.JwtKey, algorithms=["HS256"])
print(decoded)

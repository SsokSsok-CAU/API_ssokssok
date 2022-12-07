import base64
import json

def ParseJwtPayLoad(tok):
    tok = tok.split('.')[1]
    tok = tok+'='*(4-len(tok)%4)
    decode = base64.b64decode(tok)
    return json.loads(decode)
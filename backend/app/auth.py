# Simple demo auth: issue a pseudo-JWT and accept it.
import time, hmac, hashlib, base64, json
from fastapi import Depends, HTTPException, status, Header
from .config import settings

def sign(payload: dict) -> str:
    body = json.dumps(payload, separators=(',', ':'), sort_keys=True).encode()
    sig = hmac.new(settings.SECRET_KEY.encode(), body, hashlib.sha256).digest()
    return base64.urlsafe_b64encode(body).decode() + "." + base64.urlsafe_b64encode(sig).decode()

def verify(token: str) -> dict:
    try:
        b64body, b64sig = token.split(".")
        body = base64.urlsafe_b64decode(b64body.encode())
        sig = base64.urlsafe_b64decode(b64sig.encode())
        calc = hmac.new(settings.SECRET_KEY.encode(), body, hashlib.sha256).digest()
        if not hmac.compare_digest(sig, calc):
            raise ValueError("bad sig")
        payload = json.loads(body.decode())
        if payload.get("exp", 0) < int(time.time()):
            raise ValueError("expired")
        return payload
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

def demo_token(email: str):
    now = int(time.time())
    return sign({"sub": email, "exp": now + 86400})

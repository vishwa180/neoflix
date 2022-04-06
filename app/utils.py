from datetime import datetime
from flask import current_app
import jwt


def generate_token(payload):
    iat = datetime.utcnow()

    payload["sub"] = payload["user_id"]
    payload["iat"] = iat
    payload["nbf"] = iat
    payload["exp"] = iat + current_app.config.get('JWT_EXPIRATION_DELTA')

    return jwt.encode(
        payload,
        current_app.config.get("JWT_SECRET"),
        algorithm='HS256'
    ).decode('ascii')

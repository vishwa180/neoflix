import bcrypt
from .base_model import Model
from app.accessors.user_accessor import UserAccessor
from app.utils import generate_token


class User(Model):
    """
    This is the auth user model and used for authentication.
    """
    def __init__(self, name, email, plain_password=None):
        self.name = name
        self.email = email
        if plain_password:
            self.encrypted_password = self._get_encrypted_password(plain_password)

    @staticmethod
    def _get_encrypted_password(plain_password):
        """Method to encrypt the password"""

        return bcrypt.hashpw(
                plain_password.encode("utf8"),
                bcrypt.gensalt()
            ).decode('utf8')

    def register_user(self):
        """Method to register a new user in DB."""
        user_accessor = UserAccessor()

        # Check if email id is already used.
        existing_user = user_accessor.get_user_by_email(self.email)
        if existing_user is not None:
            raise Exception("Email already registered")

        # Insert the user into to DB.
        user_node = user_accessor.create_user(self)

        payload = {
            "user_id": user_node["user_id"],
            "email": user_node["email"],
            "name": user_node["name"],
        }
        payload["token"] = generate_token(payload)
        return payload

    @staticmethod
    def authenticate(email, plain_password):
        """Method to authenticate a user with email and password."""

        user = UserAccessor().get_user_by_email(email)
        if user is None:
            return False

        if bcrypt.checkpw(plain_password.encode('utf-8'), user["password"].encode('utf-8')) is False:
            return None

        payload = {
            "user_id": user["user_id"],
            "email": user["email"],
            "name": user["name"],
        }

        payload["token"] = generate_token(payload)

        return payload

from datetime import timedelta

from infrastructure.config import configs
from app.core.exceptions import AuthError
from app.core.security import create_access_token, get_password_hash, verify_password
from data.models import User
from data.repository.user_repository import UserRepository
from interface.schema.auth_schema import Payload, SignIn, SignUp
from app.services.base_service import BaseService


class AuthService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        super().__init__(user_repository)

    def sign_in(self, sign_in: SignIn):
        user: User = self.user_repository.read_by_email(sign_in.email)
        if not user:
            raise AuthError(detail="Incorrect email or password")

        if not verify_password(sign_in.password, user.password):
            raise AuthError(detail="Incorrect password")

        payload = Payload(
            id=user.id,
            email=user.email,
            first_name=user.first_name
        )
        token_lifespan = timedelta(minutes=configs.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token, expiration_datetime = create_access_token(payload.dict(), token_lifespan)
        response = {
            "access_token": access_token
        }
        return response

    def sign_up(self, sign_up: SignUp):
        user = User(**sign_up.dict(exclude_none=True))
        user.password = get_password_hash(sign_up.password)
        created = self.user_repository.create(user)
        return created

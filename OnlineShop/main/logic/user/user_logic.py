from rest_framework_simplejwt.tokens import RefreshToken

from main.dao.user.user_dao import UserDAO
from main.model.user.user_entity import User


class UserLogic:

    def __init__(self):
        self.dao = UserDAO()

    def get_user_by_id(self, user_id: int) -> User:
        return self.dao.get_user_by_id(user_id)

    def get_user_by_username(self, username: str) -> User:
        return self.dao.get_user_by_username(username)

    def create_refresh_token(self, user: User) -> tuple:
        return self.dao.create_refresh_token(user)
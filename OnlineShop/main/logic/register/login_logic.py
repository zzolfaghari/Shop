from ...logic.user.user_logic import UserLogic
from ...model.vo.register_vo import RegisterVO


class LoginLogic:

    def __init__(self):
        self.user_logic = UserLogic()

    def login(self, username: str, password: str) -> dict | ValueError:
        user = self.user_logic.get_user_by_username(username)
        if user:
            if user.check_password(password):
                access_token, refresh_token = self.user_logic.create_refresh_token(user)
                return {RegisterVO.access_token: str(access_token), RegisterVO.refresh_token: str(refresh_token)}
            else:
                raise ValueError("Password is incorrect")

        else:
            raise ValueError("User Does Not Exist!")

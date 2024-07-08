from main.dao.registration.register_dao import RegisterDAO


class RegisterLogic:
    def __init__(self):
        self.dao = RegisterDAO()
        
    def insert_user(self, **kwargs) -> None:
        return self.dao.insert_user(**kwargs)

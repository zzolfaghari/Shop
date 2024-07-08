from main.model.user.user_entity import User
from main.model.vo.register_vo import RegisterVO


class RegisterDAO:
    
    def insert_user(self, **kwargs) -> None:
        password = kwargs.pop(RegisterVO.password)
        user = User.objects.create(**kwargs)
        user.set_password(password)
        user.save()
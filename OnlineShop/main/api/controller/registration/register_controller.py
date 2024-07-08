from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from main.api.serializer.registeration.register_serializer import UserRegisterSerializer
from main.enum.user_type import UserType
from main.logic.register.register_logic import RegisterLogic
from main.model.vo.register_vo import RegisterVO
from main.shared.based_response.common_response import ErrorResponse


class RegisterController(ViewSet):
    permission_classes = [AllowAny]

    def __init__(self):
        super().__init__()
        self.register_logic = RegisterLogic()

    @extend_schema(
        request=UserRegisterSerializer,
        tags=[RegisterVO.register_tag],
        responses={201: dict}
    )
    def post(self, request: Request) -> Response | ErrorResponse:
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                username = serializer.validated_data.get(RegisterVO.username)
                password = serializer.validated_data.get(RegisterVO.password)
                email = serializer.validated_data.get(RegisterVO.email)
                first_name = serializer.validated_data.get(RegisterVO.first_name)
                last_name = serializer.validated_data.get(RegisterVO.last_name)
                self.register_logic.insert_user(username=username, password=password,
                                                email=email, first_name=first_name,
                                                last_name=last_name, type=UserType.PRODUCER.value)
                return Response(data=RegisterVO.successful_register_message, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)

        else:
            return ErrorResponse(message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

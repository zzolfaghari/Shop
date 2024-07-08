from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from main.api.serializer.registeration.login_serializer import LoginSerializer
from main.logic.register.login_logic import LoginLogic
from main.model.vo.register_vo import RegisterVO
from main.shared.based_response.common_response import ErrorResponse


class LoginController(ViewSet):
    permission_classes = [AllowAny]

    def __init__(self):
        super().__init__()
        self.logic = LoginLogic()

    @extend_schema(
        request=LoginSerializer,
        tags=[RegisterVO.register_tag],
        responses={201: dict},
    )
    def post(self, request: Request) -> Response | ErrorResponse:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            username = serializer.validated_data.get(RegisterVO.username, None)
            password = serializer.validated_data.get(RegisterVO.password, None)

            response = self.logic.login(username, password)

            return Response(data=response, status=status.HTTP_200_OK)
        except Exception as e:
            return ErrorResponse(message=str(e), status=status.HTTP_400_BAD_REQUEST)

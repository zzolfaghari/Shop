from rest_framework import status
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from main.api.serializer.product.product_serializer import ProductSerializer, ProductsListSerializer
from main.logic.product.product_logic import ProductLogic
from main.shared.based_response.common_response import CreateResponse, ErrorResponse


class ProductController(ViewSet):
    def __init__(self):
        super().__init__()
        self.logic = ProductLogic()

    def post(self, request: Request) -> CreateResponse | ErrorResponse:
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.logic.create_product(**serializer.validated_data, seller=request.user)

            return CreateResponse()
        except Exception as e:
            return ErrorResponse(message=str(e), status=status.HTTP_406_NOT_ACCEPTABLE)




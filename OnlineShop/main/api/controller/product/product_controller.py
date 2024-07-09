from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from main.api.serializer.product.product_serializer import ProductSerializer, ProductsListSerializer
from main.logic.product.product_logic import ProductLogic
from main.model.vo.product_vo import ProductVO
from main.permissions import IsProducerOrAdmin
from main.shared.based_response.common_response import CreateResponse, ErrorResponse


class ProductController(ViewSet):
    permission_classes = (IsProducerOrAdmin,)

    def __init__(self):
        super().__init__()
        self.logic = ProductLogic()

    @extend_schema(
        request={
            'multipart/form-data': ProductVO.update_or_create_product_request_schema},
        tags=[ProductVO.product_tag],
        responses={201: str}

    )
    def post(self, request: Request) -> CreateResponse | ErrorResponse:
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.logic.create_product(**serializer.validated_data, seller=request.user)

            return CreateResponse()
        except Exception as e:
            return ErrorResponse(message=str(e), status=status.HTTP_406_NOT_ACCEPTABLE)

    @extend_schema(
        request=ProductsListSerializer,
        tags=[ProductVO.product_tag],
        responses=200
    )
    def products_list(self, request: Request):
        all_products = self.logic.get_all_products(seller=request.user)
        serializer = ProductsListSerializer(all_products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=ProductsListSerializer,
        tags=[ProductVO.product_tag],
        responses=200
    )
    def products_list(self, request: Request):
        all_products = self.logic.get_all_products(seller=request.user)
        serializer = ProductsListSerializer(all_products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request={
            'multipart/form-data': ProductVO.update_or_create_product_request_schema
        },
        tags=[ProductVO.product_tag],
        responses=200
    )
    def update_product(self, request: Request, pk: int) -> Response | ErrorResponse:
        data = self.check_request_has_images(request)
        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        images = serializer.validated_data.get(ProductVO.image, None)
        title = serializer.validated_data.get(ProductVO.title, None)
        price = serializer.validated_data.get(ProductVO.price, None)
        description = serializer.validated_data.get(ProductVO.description, None)

        try:
            self.logic.update_product(product_id=pk, image=images, title=title, price=price,
                                      description=description, seller=request.user)
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return ErrorResponse(message=str(e), status=status.HTTP_400_BAD_REQUEST)

    def check_request_has_images(self, request: Request) -> dict:
        if 'image' in request.data.keys():
            if request.data['image'] == '':
                data = request.data.copy()
                data.pop('image')
            else:
                data = request.data
                return data
        return data

    @extend_schema(
        tags=[ProductVO.product_tag],
        responses=200
    )
    def delete_product(self, request: Request, pk: int) -> Response | ErrorResponse:
        try:
            self.logic.delete_product(pk, seller=request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return ErrorResponse(message=str(e), status=status.HTTP_400_BAD_REQUEST)





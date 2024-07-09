from rest_framework import status
from rest_framework.response import Response

from main.api.serializer.system.system_serializer import ResponseSerializer


class CreateResponse(Response):
    def __init__(self):
        self.default_message = 'Created Successfully'
        self.status_code = status.HTTP_201_CREATED
        response = ResponseSerializer({'message': str(self.default_message), 'status_code': self.status_code})
        super().__init__(data=response.data,
                         status=self.status_code)


class ErrorResponse(Response):
    def __init__(self, status: int, message=None):
        if message is None:
            self.error = ResponseSerializer(
                {'message': '', 'status_code': ''})
        else:
            self.error = ResponseSerializer(
                {'message': str(message), 'status_code': status})

        super().__init__(data=self.error.data, status=status)

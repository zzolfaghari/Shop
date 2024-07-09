from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status


from main.enum.user_type import UserType
from main.model.user.user_entity import User


class ProductSubmissionTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser', type=UserType.PRODUCER.value)
        self.user.set_password('Changeme')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.url = reverse('create_product')

    def login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'Changeme'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access_token']

    def test_user_can_submit_product(self):
        access_token = self.login()
        
        product_data = {
            'title': 'Test Product',
            'description': 'This is a test product description',
            'price': '12.34',

        }

        response = self.client.post(self.url, product_data, format='multipart', HTTP_AUTHORIZATION='Bearer ' + access_token)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
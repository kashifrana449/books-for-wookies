from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class UserAuthTestClass(APITestCase):

    def test_create_user(self):
        data = {'username': 'kashif', 'first_name': 'M', 'last_name': 'Kashif', 'password': 'kashif123'}
        response = self.client.post('/api/create-user/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_token(self):
        user = User(username='kashif', first_name='M', last_name='Kashif')
        user.set_password('kashif123')
        user.save()
        response = self.client.post('/api/get-token/', data={'username': 'kashif', 'password': 'kashif123'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.post('/api/refresh-token/', data={'refresh': response.data['refresh']}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import Book
User = get_user_model()


class TestBookViewSet(APITestCase):
    url = '/api/books/'
    auth_url = '/api/get-token/'

    @classmethod
    def setUpClass(cls):
        super(TestBookViewSet, cls).setUpClass()
        user1 = User(username='kashif1', first_name='M', last_name='kashif')
        user1.set_password('kashif123')
        user1.save()
        user2 = User(username='kashif2', first_name='M', last_name='kashif')
        user2.set_password('kashif123')
        user2.save()
        cls.data = {'title': 'science', 'description': 'science book', 'price': 20}
        cls.client1 = APIClient()
        cls.token1 = cls.client1.post(cls.auth_url, data={'username': user1.username, 'password': 'kashif123'}, format='json').data
        cls.token2 = cls.client1.post(cls.auth_url, data={'username': user2.username, 'password': 'kashif123'}, format='json').data

    def test_book_publish(self):
        for token in [self.token1, self.token2]:
            self.client1.credentials(HTTP_AUTHORIZATION='Bearer ' + token['access'])
            response = self.client1.post(self.url, data=self.data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_books_using_auth_user(self):
        book = Book.objects.create(**self.data, author_id=1)
        response = self.client1.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_a_book_using_auth_user(self):
        book = Book.objects.create(**self.data, author_id=1)
        response = self.client1.get(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book_data(self):
        book = Book.objects.create(**self.data, author_id=1)
        self.client1.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token1['access'])
        response = self.client1.patch(f'/api/books/{book.id}/', data={'price': 21}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['price'], 21)

    def test_update_book_data_using_other_author(self):
        book = Book.objects.create(**self.data, author_id=1)
        self.client1.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token2['access'])
        response = self.client1.patch(f'/api/books/{book.id}/', data={'price': 21}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_data_using_author(self):
        book = Book.objects.create(**self.data, author_id=1)
        self.client1.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token1['access'])
        response = self.client1.delete(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_book_data_using_other_author(self):
        book = Book.objects.create(**self.data, author_id=1)
        self.client1.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token2['access'])
        response = self.client1.delete(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_data_using_non_auth_user(self):
        book = Book.objects.create(**self.data, author_id=1)
        self.client1._credentials = {}
        response = self.client1.delete(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

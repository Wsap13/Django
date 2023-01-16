from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from . import views
from .models import BookCategory,Client, Book
from rest_framework import status
from django.utils.http import urlencode
from django import urls
from django.contrib.auth.models import User


class BookCategoryTests(APITestCase):
    def post_book_category(self, name):
        url = reverse(views.BookCategoryList.name)
        data = {'name':name}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_book_category(self):
        new_book_category_name = 'IT'
        response = self.post_book_category(new_book_category_name)
        print("PK {0}".format(BookCategory.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert BookCategory.objects.count() == 1
        assert BookCategory.objects.get().name == new_book_category_name

    def test_post_existing_book_category_name(self):
        url = reverse(views.BookCategoryList.name)
        new_book_category_name = 'Duplicate IT'
        data = {'name':new_book_category_name}
        response_one = self.post_book_category(new_book_category_name)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_book_category(new_book_category_name)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_book_category_by_name(self):
        book_category_name_one = 'IT'
        book_category_name_two = 'Romance'
        self.post_book_category(book_category_name_one)
        self.post_book_category(book_category_name_two)
        filter_by_name = {'name': book_category_name_one}
        url= '{0}?{1}'.format(reverse(views.BookCategoryList.name), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == book_category_name_one

    def test_get_book_categories_collection(self):
        new_book_category_name = 'Super Copter'
        self.post_book_category(new_book_category_name)
        url = reverse(views.BookCategoryList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == new_book_category_name

    def test_update_book_category(self):
        book_category_name = 'IT'
        response = self.post_book_category(book_category_name)
        url = urls.reverse(views.BookCategoryDetail.name,None,{response.data['pk']})
        updated_book_category_name = 'New IT'
        data = {'name': updated_book_category_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == updated_book_category_name

    def test_get_book_category(self):
        book_category_name = 'IT'
        response = self.post_book_category(book_category_name)
        url = urls.reverse(views.BookCategoryDetail.name,None,{response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['name'] == book_category_name

class ClientTests(APITestCase):
    def create_client(self,  first_name, last_name,gender, address, birthdate, client):
        url = reverse(views.ClientList.name)
        data = { 'first_name':first_name,
                 'last_name': last_name,
                 'gender': gender,
                 'address':address,
                 'birthdate':birthdate,}
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_client(self):
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        client = APIClient()
        client.login(username='admin', password='admin123')
        new_first_name = 'Jan'
        new_last_name = 'Kowalski'
        new_gender = 'M'
        new_address = 'Dworcowa 20'
        new_birthdate = '1999-01-01'
        response = self.create_client(new_first_name,new_last_name,new_gender,new_address,new_birthdate, client)
        assert response.status_code == status.HTTP_201_CREATED
        assert Client.objects.count() == 1
        assert Client.objects.get().first_name == new_first_name
        assert Client.objects.get().last_name == new_last_name

class BookTests(APITestCase):
    def create_book_category(self, client):
        url = reverse(views.BookCategoryList.name)
        data = {'id': 1,'name':'criminal'}
        client.post(url, data, format='json')


    def create_book(self, title, book_category, publication_date, author, owner, client):
        url = reverse(views.BookList.name)
        data = {'title': title,
                'book_category': book_category,
                'publication_date': publication_date,
                'author': author,
                'owner': owner}
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_book(self):
        user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        client = APIClient()
        client.login(username='admin', password='admin123')
        self.create_book_category(client)
        new_title = 'Pan Tadeusz'
        new_book_category = 'criminal'
        new_publication_date = '1999-01-01'
        new_author = 'Mickiewicz'
        response = self.create_book(new_title,new_book_category,new_publication_date,new_author,user.id, client)
        assert response.status_code == status.HTTP_201_CREATED
        assert Book.objects.count() == 1
        assert Book.objects.get().title == new_title
        assert Book.objects.get().author == new_author

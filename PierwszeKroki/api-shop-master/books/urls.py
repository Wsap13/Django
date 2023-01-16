from django.urls import path
from . import views

urlpatterns = [
    path('book-categories',views.BookCategoryList.as_view(), name=views.BookCategoryList.name),
    path('book-categories/<int:pk>',views.BookCategoryDetail.as_view(), name=views.BookCategoryDetail.name),
    path('books', views.BookList.as_view(), name=views.BookList.name),
    path('books/<int:pk>', views.BookDetail.as_view(), name=views.BookDetail.name),
    path('clients', views.ClientList.as_view(), name=views.ClientList.name),
    path('clients/<int:pk>', views.ClientDetail.as_view(), name=views.ClientDetail.name),
    path('orders', views.OrderList.as_view(), name=views.OrderList.name),
    path('orders/<int:pk>', views.OrderDetail.as_view(), name=views.OrderDetail.name),
    path('users', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    ]

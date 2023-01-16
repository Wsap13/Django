from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Book,BookCategory, Client, Order
from .serializers import BookCategorySerializer, BookSerializer, OrderSerializer, ClientSerializer, UserSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User
from .custompermission import IsCurrentUserOwnerOrReadOnly


class BookCategoryList(generics.ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    name = 'bookcategory-list'
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


class BookCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    name = 'bookcategory-detail'



class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'
    filter_fields = ['title', 'book_category', 'publication_date', 'added_time', 'author']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'book_category', 'author']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly,)

class ClientFilter(FilterSet):
    from_birthdate = DateTimeFilter(field_name='birthdate', lookup_expr='gte')
    to_birthdate = DateTimeFilter(field_name='birthdate', lookup_expr='lte')

    class Meta:
        model = Client
        fields = ['from_birthdate','to_birthdate']

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_class = ClientFilter
    name = 'client-list'
    ordering_fields = ['last_name', 'birthdate']


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class OrderFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    client_name = AllValuesFilter(field_name='client__last_name')

    class Meta:
        model = Order
        fields = ['min_price', 'max_price', 'client_name']


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_class = OrderFilter
    name = 'order-list'


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    name = 'order-detail'


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'book-categories': reverse(BookCategoryList.name, request=request),
                         'books': reverse(BookList.name, request=request),
                         'clients': reverse(ClientList.name, request=request),
                         'orders': reverse(OrderList.name, request=request),
                         'users': reverse(UserList.name, request=request)
})
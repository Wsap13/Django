from rest_framework import serializers
from .models import Order, Book, BookCategory, Client
from django.contrib.auth.models import User

class BookCategorySerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='book-detail')
    class Meta:
        model = BookCategory
        fields = ['pk', 'url', 'name', 'books']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    book_category = serializers.SlugRelatedField(queryset=BookCategory.objects.all(), slug_field='name')
    orders = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='order-detail')
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Book
        fields = ['url', 'title', 'book_category', 'owner', 'publication_date', 'added_time', 'author', 'orders']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    orders = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='order-detail')
    gender = serializers.ChoiceField(choices=Client.GENDER_CHOICES)
    class Meta:
        model = Client
        fields = ['url','pk','first_name', 'last_name', 'gender', 'birthdate','added_time','orders']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='last_name')
    book =  serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='title')
    class Meta:
        model = Order
        fields = ['pk','url','client','book','price', 'quantity']

    def validate_price(self, value):
        if value<=0:
            raise serializers.ValidationError("Don't make price lower or equal to zero", )
        return value

    def validate_quantity(self, value):
        if value<=0:
            raise serializers.ValidationError("Don't make quantity lower or equal to zero", )
        return value

class UserBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url','title']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    books = UserBookSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ['url','pk','username','books']
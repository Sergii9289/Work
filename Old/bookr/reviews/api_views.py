from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView

from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer

class Login(APIView):
    def post(self, request):
        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        # автентифікація користувача. Якщо дані коректні, то отримаємо користувача.
        if not user:
            return Response({'error': 'Credentials are incorrect or user does not exist'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = []  #  Це означає, що ваше представлення (view) буде вимагати передачі
    # дійсного токена в заголовку запиту для доступу до нього.
    permission_classes = []  # лише користувачі, які мають дійсний токен або сесію,
    # зможуть отримати доступ до цього представлення.


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.order_by(
        '-date_created')  # сортування в обратному порядку по полю date_created
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination  # пагінація як на сайті Віяра. На сторінці N елементів
    # і багато сторінок з N елементів
    authentication_classes = []  # порожній список означає, що автентифікація не потрібна для перегляду

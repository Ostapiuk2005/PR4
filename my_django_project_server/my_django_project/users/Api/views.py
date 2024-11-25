from rest_framework import generics
from users.models.user import CustomUser
from users.serializer.users import CustomUserSerializer
from rest_framework.permissions import IsAdminUser
from drf_spectacular.utils import extend_schema


@extend_schema(summary="отримання списку всіх користувачів")
class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]


@extend_schema(summary="отримання деталей про конкретного користувача")
class UserRetrieve(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]


@extend_schema(summary="створення нового користувача", description='додає нового користувача')
class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]


@extend_schema(summary="оновлення даних про користувача")
class UserUpdate(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
    

@extend_schema(summary="видалення користувача", description='видаляє користувача з бд')
class UserDestroy(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
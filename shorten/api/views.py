from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
    name = 'user-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class PerfilList(generics.ListCreateAPIView):
	queryset = Perfil.objects.all()
	serializer_class = PerfilSerilizer
	name = 'perfil-list'
class PerfilDetail(generics.ListCreateAPIView):
	queryset = Perfil.objects.all()
	serializer_class = PerfilSerilizer
	name = 'perfil-detail'

class ShortenedList(generics.ListAPIView):
	queryset = Shortened.objects.all()
	serializer_class = ShortenedListSerializer
	name = 'shortened-list'

class ShortenedCreate(generics.CreateAPIView):
	queryset = Shortened.objects.all()
	serializer_class = ShortenedSerializer
	name = 'shortened-create'

class ShortenedDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Shortened.objects.all()
	serializer_class = ShortenedListSerializer
	name = 'shortened-detail'
from rest_framework import generics
from django.urls import path
from . import views

urlpatterns = [
	path('shortened/', views.ShortenedCreate.as_view(), name=views.ShortenedCreate.name),
	path('shorteneds/', views.ShortenedList.as_view(), name=views.ShortenedList.name),
	path('shorteneds/<int:pk>', views.ShortenedDetail.as_view(), name=views.ShortenedDetail.name),
	path('user/', views.UserList.as_view(), name=views.UserList.name),
	path('user/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
	path('perfil/', views.PerfilList.as_view(), name=views.PerfilList.name),
	path('perfil/<int:pk>/', views.PerfilDetail.as_view(), name=views.PerfilDetail.name),
]
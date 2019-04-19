from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('shorten',views.shorten, name='shorten'),
    path('report', views.shotened_report, name='report'),
    path('<slug:shortened>', views.go_to_url, name='go'),
]

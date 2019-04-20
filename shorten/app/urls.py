from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('shorten',views.shorten, name='shorten'),
    path('report', views.shotened_report, name='report'),
    path('adduser',views.create_user, name='adduser'),
    path('<slug:shortened>', views.go_to_url, name='go'),
    path('login/',views.do_login, name='login'),
    path('logout/',views.do_logout, name='logout'),
    
]

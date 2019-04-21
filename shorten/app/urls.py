from django.contrib.auth import views as v
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('shorten/',views.shorten, name='shorten'),
    path('report/', views.shotened_report, name='report'),
    path('adduser/',views.create_user, name='adduser'),
    path('acount/login/', v.LoginView.as_view()),
    path('acount/logout/', v.LogoutView.as_view()),
    path('login/', views.do_login, name='login'),
    path('logout/', views.do_logout, name="logout"),
    path('<slug:shortened>', views.go_to_url, name='go'),
    
]

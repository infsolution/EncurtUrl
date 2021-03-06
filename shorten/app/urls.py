from django.contrib.auth import views as v
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('shorten/',views.shorten, name='shorten'),
    path('report/', views.shotened_report, name='report'),
    path('report/<int:shortened_id>/', views.detail, name='detail'),
    path('adduser/',views.create_user, name='adduser'),
    path('login/', v.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', v.LogoutView.as_view(template_name='app/login.html'), name='logout'),
    path('access/', views.access_private,name='private'),
    path('contatos/', views.get_contatos, name='contatos'),
    path('request-access/<slug:codeurl>/', views.request_access, name='request_access'),
    path('<slug:shortened>', views.go_to_url, name='go'),
    path('about/', views.about, name='about'),
    path('help/',views.help, name='help'),
    path('personalize/<int:shortened_id>/', views.personalize, name='personalize'),
    path('valid/<int:shortened_id>/', views.valid, name='valid'),
]


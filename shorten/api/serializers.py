from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import *
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','id','username','email', 'password')

class PerfilSerilizer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Perfil
		fields = ('url','id','name', 'user')

class ShortenedListSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Shortened
		fields = ('url','id', 'url_user', 'url_shortened', 'created_at', 'expiring_date', 'code', 'private_code', 'preview_message', 'perfil')

class ShortenedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Shortened
		fields = ('url')
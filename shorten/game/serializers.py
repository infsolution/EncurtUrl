from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','id','username','email', 'password')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('url', 'id', 'name', 'user','created_at', 'escore')
class ScoreSeiralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('url', 'id', 'name', 'escore')
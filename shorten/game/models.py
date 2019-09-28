from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=255, default='', unique=True)
	user = models.OneToOneField(User, related_name='player', on_delete=models.CASCADE)
	email_validated = models.BooleanField(default=False)
	created_at = models.DateField(auto_now_add=True)
	escore = models.IntegerField(default=0)
	class Meta:
		ordering = ('-escore',)
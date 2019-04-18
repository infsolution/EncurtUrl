from django.contrib.auth.models import User
from django.db import models
from random import randint

class Shortened(models.Model):
	user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, null=True)
	url = models.CharField(max_length=1024)
	url_shortened = models.CharField(max_length=256, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	expiring_date = models.DateTimeField(auto_now_add=False, null=True)
	code = models.CharField(max_length=12, null=True)

	def shorten(self):
		self.url_shortened = self.get_code()


	def get_code(self):
		code = ''
		for num in range(0,6):
			char = randint(1,4)
			if char == 1:
				code += str(chr(randint(48,57)))
			elif char == 2:
				code += str(chr(randint(65,90)))
			else:
				code += str(chr(randint(97,122)))
		return code


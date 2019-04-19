from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from random import randint
import datetime
class Shortened(models.Model):
	user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, null=True)
	url = models.CharField(max_length=1024)
	url_shortened = models.CharField(max_length=256, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	expiring_date = models.DateTimeField(auto_now_add=False, null=True)
	code = models.CharField(max_length=12, null=True)

	def shorten(self):
		self.url_shortened = self.get_code()
		self.set_expiring_date()

	def set_expiring_date(self):
		if self.user == None:
			self.expiring_date = timezone.now() + datetime.timedelta(days=30)
	



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


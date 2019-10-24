from django.db import models
from django.contrib.auth.models import User
from PIL import Image

#Handles profiles
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#Profile picture
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	#Prints out profile information
	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		#Resizes image to save space on database
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)


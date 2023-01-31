from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from PIL import Image

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content

class Follower(models.Model):
    user = models.ForeignKey(User, related_name='following',on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followed_by',on_delete=models.CASCADE)
    def __str__(self):
        return self.following.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'
        # Override the save method of the model
    # for save issue
    # https://stackoverflow.com/questions/52351756/django-typeerror-save-got-an-unexpected-keyword-argument-force-insert
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image
        if img.mode != 'RGB':
            img = img.convert('RGB')

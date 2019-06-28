from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userProfile(models.Model):
    user = models.OneToOneField(User)

    profilePic = models.ImageField(upload_to='userProfilePic',blank=True)
    portfolioUrl = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

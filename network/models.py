from django.contrib.auth.models import AbstractUser
from django.db import models

# Inherits from AbstractUser - has access to username, email, password, etc.
class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_media/', blank=True, null=True)

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="foo")
    followed_by = models.ManyToManyField(User, blank=True, related_name="following")
    
    def __str__(self):
        return f"{self.user} is followed by: {self.followed_by}"

class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tweetText = models.CharField(max_length=255)
    tweetImage = models.ImageField(upload_to='tweet_media/', blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, blank=True, related_name="likes")

    def __str__(self):
        return f"{self.author} tweeted: {self.tweetText} image: {self.tweetImage}"

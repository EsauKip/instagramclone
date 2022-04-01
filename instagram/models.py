from time import timezone
from django.db import models
from  django.utils import timezone
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True)
    caption=models.TextField()
    date_created=models.DateTimeField(default=timezone.now)
      
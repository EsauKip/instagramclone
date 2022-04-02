from time import timezone
from django.db import models
from  django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    image_name = models.CharField(max_length=80,blank=True)
    image_profile=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True)
    caption=models.TextField()
    date_created=models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    comments = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.image_name 
    def save_image(self):
        return self.save()
    def delete_image(self):
        self.delete()
    @classmethod
    def search_image(cls, name):
        return cls.objects.filter(image_name__image__name__icontains=name)
    
    @classmethod
    def get_image_by_id(cls, image_id):
        image = cls.objects.get(id=image_id)
        return image
        
    def add_likes(self):
        return self.likes.count()  
class Comment(models.Model):
    comment = models.TextField()
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    user= models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)


   
            

        
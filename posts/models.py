from django.db import models
from django.conf import settings

User=settings.AUTH_USER_MODEL

class Post(models.Model):
    title=models.CharField(max_length=255, blank=True, null=True)
    content=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True, blank=True, null=True)

    updated_at=models.DateTimeField(auto_now=True,  blank=True, null=True)
    author=models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True)

    likes=models.ManyToManyField(User,related_name='blog_post')
    def total_likes(self):
        return self.likes.count()

#class Comments(models.Model):
    
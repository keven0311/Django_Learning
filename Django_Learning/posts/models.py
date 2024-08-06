from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png',blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None) 
    # ABOVE: sign relationship between User and Post.
    #        on_delete means if the user get deleted, his posts will also get delete
    
    def __str__(self):
        return self.title
    



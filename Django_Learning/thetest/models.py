from django.db import models

# Create your models here.
class Test(models.Model):
    id = models.UUIDField(auto_created=True,primary_key=True)
    name = models.TextField()
    email = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
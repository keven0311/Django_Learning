from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    about = models.TextField(max_length=200)
    date = models.DateField(auto_now_add=True)
    avatar = models.ImageField(default='pythonlogo.png',blank=True)
    
    
    def __str__(self):
        return self.name
    
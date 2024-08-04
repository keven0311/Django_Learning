from django.db import models
import uuid

# Create your models here.
class Test(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
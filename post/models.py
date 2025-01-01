from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)

    image = models.ImageField(upload_to='images')
    product = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField()

    province = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    ward = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def formatted_created_at(self):
        return self.created_at.strftime('%d/%m/%Y')
from django.db import models
from apps.categories.models import Category
from autoslug import AutoSlugField


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    
   


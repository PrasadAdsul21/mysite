from django.db import models
from django.db.models import Model

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    name=models.CharField(max_length=25)
    decs=models.CharField(max_length=50)
    price=models.FloatField()
    image=models.ImageField(upload_to='product/image')
    def  __str__(self):
        return self.name
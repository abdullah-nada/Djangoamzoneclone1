from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.utils import timezone


# Create your models here.
flag_file=(('new',"new"),('sale',"sale"),('feature','feature'))

class Product(models.Model):
    name = models.CharField(max_length=120)
    flag=models.CharField(max_length=10,choices=flag_file)
    price=models.FloatField()
    img=models.ImageField( upload_to='pro_img')
    sku=models.IntegerField()
    subtitle=models.TextField(max_length=500)
    description=models.TextField(max_length=1000)
    tags = TaggableManager()
    brand=models.ForeignKey("Brand",related_name='pro_brand' ,on_delete=models.SET_NULL,null=True)


class Productimg(models.Model):
    product=models.ForeignKey("Product",related_name='pr_img', on_delete=models.CASCADE)
    img=models.ImageField(upload_to='product_img')



class Brand(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='brand')
    

class Review(models.Model):
    user=models.ForeignKey( User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey("Product",related_name='review_product' ,on_delete=models.CASCADE)
    review=models.TextField(max_length=400)
    rate=models.IntegerField(choice=[(i,i) for i in range(1,6)])
    date=models.DateTimeField(defalut=timezone.now)

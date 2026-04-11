from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
flag_file=(('new',"new"),('sale',"sale"),('feature','feature'))

class Product(models.Model):
    name = models.CharField(_("name"),max_length=120)
    flag=models.CharField(_("flag"),max_length=10,choices=flag_file)
    price=models.FloatField(_("price"))
    img=models.ImageField(_("img"),upload_to='pro_img')
    sku=models.IntegerField(_("sku"))
    subtitle=models.TextField(_("subtitle"),max_length=500)
    description=models.TextField(_("description"),max_length=1000)
    tags = TaggableManager()
    brand=models.ForeignKey("Brand",related_name='pro_brand',verbose_name=_('brand'),on_delete=models.SET_NULL,null=True)
    slug=models.SlugField(blank=True, null=True)

    def save (self,*args ,**kwargs):
        self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)


class Productimg(models.Model):
    product=models.ForeignKey("Product",related_name='pr_img',verbose_name=_('product'), on_delete=models.CASCADE)
    img=models.ImageField(_("img"),upload_to='product_img')



class Brand(models.Model):
    name=models.CharField(_("name"),max_length=50)
    img=models.ImageField(_("img"),upload_to='brand')
    slug=models.SlugField(blank=True, null=True)

    def save (self,*args ,**kwargs):
        self.slug=slugify(self.name)
        super(Brand,self).save(*args ,**kwargs)

class Review(models.Model):
    user=models.ForeignKey(User,verbose_name=_('user'),on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey("Product",related_name='review_product',verbose_name=_('product') ,on_delete=models.CASCADE)
    review=models.TextField(_("review"),max_length=400)
    rate=models.IntegerField(_("rate"),choice=[(i,i) for i in range(1,6)])
    date=models.DateTimeField(defalut=timezone.now)



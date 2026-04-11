from django.contrib import admin

# Register your models here.


from .models import Product,Productimg,Brand ,Review


class Productimginline(admin.TabularInline):
    model=Productimg


class ProductAdmin(admin.ModelAdmin):
    inlines=[Productimginline]



admin.site.register( Product,ProductAdmin)
admin.site.register( Productimg)
admin.site.register( Brand)
admin.site.register(Review)
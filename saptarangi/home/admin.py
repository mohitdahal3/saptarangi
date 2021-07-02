from django.contrib import admin
from .models import Available_product , Sold_product

# Register your models here.
admin.site.register(Available_product)
admin.site.register(Sold_product)
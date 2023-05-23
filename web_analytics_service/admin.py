from django.contrib import admin

# Register your models here.
from .models import (Iphone, Shop, DateAdd)

admin.site.register(Iphone)
admin.site.register(Shop)
admin.site.register(DateAdd)

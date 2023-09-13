from django.contrib import admin
from . import models
from django.utils.html import format_html
# Register your models here.


class Caradmin(admin.ModelAdmin):
    def tumbnail(self, object):
        return format_html('<img src="{}" width=40px style=border-radius:50px;'.format(object.car_photo.url))


    tumbnail.short_description = 'Car_image'
    list_display=('id','tumbnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('car_title','id')
    # search_fields = ('first_name', 'last_name')

admin.site.register(models.Car, Caradmin)

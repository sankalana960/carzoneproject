from django.contrib import admin
from . import models
from django.utils.html import format_html
# Register your models here.

class Teamadmin(admin.ModelAdmin):
    def tumbnail(self, object):
        return format_html('<img src="{}" width=40px style=border-radius:50px;'.format(object.photo.url))


    tumbnail.short_description = 'photo'
    list_display=('id','tumbnail', 'first_name', 'designation', 'created_date')
    list_display_links = ('first_name','id')
    search_fields = ('first_name', 'last_name')


admin.site.register(models.Team, Teamadmin)
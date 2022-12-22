from django.contrib import admin
from Movieapp.models import Movies

#Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    list_display=['releasedate','moviename', 'actor','actress','rating'];

admin.site.register(Movies,MoviesAdmin);


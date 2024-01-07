from django.contrib import admin
from ImageGallery.models import Image 
# Register your models here.

class AdminReg(admin.ModelAdmin):
    list_display=("imageName","mainImage","category","imageSlug")


admin.site.register(Image,AdminReg)
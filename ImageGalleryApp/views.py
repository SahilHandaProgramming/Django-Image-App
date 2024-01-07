from django.shortcuts import render
from ImageGallery.models import Image
def mainPage(req):
    objects = Image.objects.all()
    diction={
        "allObj":objects
    }
    return render(req,"index.html",diction)

def searchCategory(req):
    name = req.GET.get("text")
    objects = Image.objects.filter(category__icontains=name)
    diction={
        "obj":objects
    }
    return render(req,"filterImage.html",diction) 


def searchOneImage(req,slug):
    objects = Image.objects.get(imageSlug=slug)
    diction={
        "obj":objects,
    }
    return render(req,"showOneImage.html",diction)


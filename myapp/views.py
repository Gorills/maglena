from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from turn.models import Slider, Turn
from .models import Worker, Awards
# Create your views here.

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def index(request):
    slide = Slider.objects.all()
    context = {
        'slides': slide,
        'turns': Turn.objects.all()[:6]
    }
    return render(request, "myapp/index.html", context)

def about(request):
    context = {
        'workers': Worker.objects.all(),
        'awards': Awards.objects.all()
    }
    return render(request, "myapp/about.html", context)

def tour(request):
  
    
    context = {
        
    }
    return render(request, "myapp/tour.html", context)


def vacancy(request):
  
    
    context = {
        
    }
    return render(request, "myapp/vacancy.html", context)

def contacts(request):
    
    context = {
        
    }
    return render(request, "myapp/contacts.html", context)

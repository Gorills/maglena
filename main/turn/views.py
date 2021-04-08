from django.shortcuts import render
from .models import Turn, Servise, Slider
from django.views.generic import ListView, DetailView

# Create your views here.
def turn(request):
    turn = Turn.objects.all()
    
    context = {
        'turns': turn,
        
    }
    return render(request, "turn/index.html", context)




def turn_detail(request, slug):
    
    context = {
        'turn': Turn.objects.get(slug=slug),
    }
    return render(request, "turn/turn_detail.html", context)



def servise_list(request, slug, parent):
    servise = Servise.objects.get(slug=slug)
    
    context = {
        'servise': servise,
    }
    return render(request, "turn/service_list.html", context)
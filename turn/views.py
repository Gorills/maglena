from django.shortcuts import get_object_or_404, render
from .models import Turn, Servise, Slider, Work
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

    

def work(request):

    context = {

        'works': Turn.objects.all()
    }
    
    return render(request, 'turn/work_list.html', context)


def work_detail(request, slug):

    context = {

        'work': get_object_or_404(Turn, slug=slug)
    }

    return render(request, 'turn/work_detail.html', context)
    
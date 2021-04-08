from django.shortcuts import render, redirect
from .models import Rewiew
from .forms import RewiewForm


# Create your views here.

def rewiew(request):

    context = {
        'rewiews': Rewiew.objects.filter(moderate=True)
    }

    return render(request, 'clients/rewiew.html', context)


def rewiew_create(request):

    error = ''
    if request.method == 'POST':
        form = RewiewForm(request.POST)
        
        if form.is_valid():
        
            form.save()
            return redirect('index')
        else:
            error = 'Не верно заполнены данные'

    form = RewiewForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, "clients/rewiew_create.html", data)



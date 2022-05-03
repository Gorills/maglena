from email import message
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Rewiew, Contact
from .forms import RewiewForm, ContactForm
from .telegram import send_message
from django.core.mail import BadHeaderError, send_mail

# Create your views here.

# class ContactView(CreateView):
#     model = Contact
#     form_class = ContactForm
#     success_url = '/'

#     def form_valid(self, form):
#         name = form.cleaned_data['name']
#         tel = form.cleaned_data['tel']
#         messages = form.cleaned_data['messages']
#         message = "Заявка с сайта maglena.tomsk.ru:" + "\n" + "*ИМЯ*: " +str(name) + "\n" + "*ТЕЛЕФОН*: " + str(tel) + "\n" + "*СООБЩЕНИЕ*: " +str(messages)
#         send_message(message)
#         send_mail(
#             'Заявка с сайта magena.tomsk.ru',
#             message,
#             'info@maglena.tomsk.ru',
#             ['gorivanickiy@gmail.com', 'order-maglena@yandex.ru', 'salonmaglena@yandex.ru'],
#             fail_silently=False,
            
#         )

#         # return super(ContactView, self).form_valid(form)
#         return redirect('/')
    
        
def contacts_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST['name']
        tel = request.POST['tel']
        messages = request.POST['messages']
        message = "Заявка с сайта maglena.tomsk.ru:" + "\n" + "*ИМЯ*: " +str(name) + "\n" + "*ТЕЛЕФОН*: " + str(tel) + "\n" + "*СООБЩЕНИЕ*: " +str(messages)
        if form.is_valid():

            send_mail('Заявка с сайта magena.tomsk.ru',message,'info@maglena.tomsk.ru',['gorivanickiy@gmail.com', 'order-maglena@yandex.ru', 'salonmaglena@yandex.ru'])
            send_message(message)
            form.save()

            return redirect('/')

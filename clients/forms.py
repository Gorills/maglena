from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Rewiew, Contact
from tinymce.widgets import TinyMCE

class RewiewForm(forms.ModelForm):
    captcha = ReCaptchaField()
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 25, 'rows': 25}))

    class Meta:
        model = Rewiew
        fields = ['name', 'email', 'text', 'captcha']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input',
                'placeholder': 'Email'
            })
        }

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta: 
        model = Contact
        fields = ['name', 'tel', 'messages', 'captcha']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'popup__input',
                'placeholder': 'Имя',
                'pattern' : '[А-Яа-яЁё ]+',
            }),
            'tel': forms.TextInput(attrs={
                'class': 'popup__input',
                'placeholder': '+7(999) 999 99-99',
                'type': 'tel',
                'pattern' : '[0-9 ]+',
            }),
            'messages': forms.Textarea(attrs={
                'class': 'popup__input',
                'placeholder': 'Сообщение',
                'pattern' : '[А-Яа-яЁё ]+',
            })
        }
        labels = {
            'name': '',
            'tel': '',
            'messages': '',

        }
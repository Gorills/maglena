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

class ContactForm(forms.Form):
    captcha = ReCaptchaField()

    class Meta: 
        model = Contact
        fields = ['name', 'tel', 'messages', 'captcha']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Имя'
            }),
            'tel': forms.EmailInput(attrs={
                'class': 'input',
                'placeholder': '+7(999) 999 99-99'
            }),
            'text': forms.Textarea(attrs={
                'class': 'input',
                'placeholder': 'Текст отзыва'
            })
        }
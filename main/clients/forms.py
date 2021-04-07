from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Rewiew


class RewiewForm(forms.ModelForm):
    # captcha = ReCaptchaField()

    class Meta:
        model = Rewiew
        fields = ['name', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input',
                'placeholder': 'Email'
            }),
            'text': forms.Textarea(attrs={
                'class': 'input',
                'placeholder': 'Текст отзыва'
            })
        }
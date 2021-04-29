from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import Config, Social, Phone, Meta, Adres, Vacancy, Worker, Awards


from djsingleton.admin import SingletonAdmin

class SocialAdmin(admin.TabularInline):
    model = Social
    extra = 0
    min_num = 1

class PhonesAdmin(admin.TabularInline):
    model = Phone
    extra = 0
    min_num = 1

class AdressAdmin(admin.TabularInline):
    model = Adres
    extra = 0
    min_num = 1

class ConfigForm(forms.ModelForm):
    about = forms.CharField(label='О нас', widget=CKEditorUploadingWidget())
    time = forms.CharField(label='Время работы', widget=CKEditorUploadingWidget())
    class Meta:
        model = Config
        fields = '__all__'


class ConfigAdmin(SingletonAdmin):
    list_display = ('name', 'email', 'time', 'logo', 'map', 'about')
    fields = ('name', 'email', 'time', 'logo', 'map', 'about')
    save_on_top = True
    form = ConfigForm
    inlines = [
        PhonesAdmin,
        AdressAdmin,
        SocialAdmin,
        
    ]
admin.site.register(Config, ConfigAdmin)



class MetaAdmin(SingletonAdmin):
    list_display = ('meta_title', 'meta_description', 'meta_subtitle', 'meta_keywords', 'domen')
    save_on_top = True


admin.site.register(Meta, MetaAdmin)

class VacancyAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Vacancy
        fields = '__all__'

class VacancyAdmin(SingletonAdmin):
    
    form = VacancyAdminForm
    
    
admin.site.register(Vacancy, VacancyAdmin)


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')

admin.site.register(Worker, WorkerAdmin)



class AwardsAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

admin.site.register(Awards, AwardsAdmin)
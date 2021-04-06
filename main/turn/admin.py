from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


from .models import Turn, Price, Servise


class PriceAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Price
        fields = '__all__'

class PriceAdmin(admin.TabularInline):
    form = PriceAdminForm
    model = Price
    extra = 0
    min_num = 1


class PriceAdminRegister(admin.ModelAdmin):
    model = Servise
    form = PriceAdminForm
    list_display = ('title', 'parent')
    fields = ('title', 'parent', 'text')

admin.site.register(Price, PriceAdminRegister)


class ServiseAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Servise
        fields = '__all__'

class ServiseAdmin(admin.StackedInline):
    form = ServiseAdminForm
    model = Servise
    extra = 0
    min_num = 1

class ServiseAdminRegister(admin.ModelAdmin):
    list_display = ('title', 'parent')
    prepopulated_fields = {'slug': ('title',)}
    model = Servise
    form = ServiseAdminForm
    # class Meta:
    #     ordering = ("parent")

admin.site.register(Servise, ServiseAdminRegister)



class TurnAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Turn
        fields = '__all__'

class TurnAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    form = TurnAdminForm
    inlines = [
        
        PriceAdmin,
        ServiseAdmin,
    ]
    
admin.site.register(Turn, TurnAdmin)
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


from .models import Turn, Price, Servise, Slider, Work, WorkImage, VideoServises, VideoTurn


class PriceAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Price
        fields = '__all__'

class PriceAdmin(admin.TabularInline):
    form = PriceAdminForm
    model = Price
    extra = 0
    min_num = 0


class PriceAdminRegister(admin.ModelAdmin):
    model = Servise
    form = PriceAdminForm
    list_display = ('title', 'parent')
    fields = ('title', 'parent', 'text')

admin.site.register(Price, PriceAdminRegister)

class VideoServisesAdmin(admin.TabularInline):
    model = VideoServises
    extra = 0
    min_num = 0



class ServiseAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Servise
        fields = '__all__'

class ServiseAdmin(admin.StackedInline):
    form = ServiseAdminForm
    prepopulated_fields = {'slug': ('title',)}
    model = Servise
    extra = 0
    min_num = 0

class ServiseAdminRegister(admin.ModelAdmin):
    list_display = ('title', 'parent')
    prepopulated_fields = {'slug': ('title',)}
    model = Servise
    form = ServiseAdminForm
    inlines = [
        VideoServisesAdmin,
    ]
    
    # class Meta:
    #     ordering = ("parent")

admin.site.register(Servise, ServiseAdminRegister)



class VideoTurnAdmin(admin.TabularInline):
    model = VideoTurn
    extra = 0
    min_num = 0




class TurnAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Turn
        fields = '__all__'

class TurnAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    form = TurnAdminForm
    save_as = True
    save_on_top = True
    inlines = [
        
        PriceAdmin,
        ServiseAdmin,
        VideoTurnAdmin,
    ]
    
admin.site.register(Turn, TurnAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')


admin.site.register(Slider, SliderAdmin)

class WorkImageAdmin(admin.StackedInline):
    model = WorkImage
    extra = 0
    min_num = 0


class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent')
    prepopulated_fields = {'slug': ('title',)}

    inlines = [
        WorkImageAdmin,
    ]

admin.site.register(Work, WorkAdmin)
from django.contrib import admin
from .models import Rewiew, Contact, Status
# Register your models here.

class RewiewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'moderate')
    list_editable = ('moderate', )

admin.site.register(Rewiew, RewiewAdmin)


class StatusAdmin(admin.TabularInline):
    list_display = ('title')
    model = Status
    extra = 0
    min_num = 1

class ContactAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'tel', 'date')
    inlines = [
        
        StatusAdmin,
      
    ]

admin.site.register(Contact, ContactAdmin)

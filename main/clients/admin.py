from django.contrib import admin
from .models import Rewiew, Contact, Status
# Register your models here.

class RewiewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'moderate')
    list_editable = ('moderate', )

admin.site.register(Rewiew, RewiewAdmin)




class ContactAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'tel', 'date', 'parent')
    list_editable = ('parent', )
    readonly_fields = ('name', 'tel', 'date', 'messages')
   

admin.site.register(Contact, ContactAdmin)


admin.site.register(Status)
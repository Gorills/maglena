from django.contrib import admin
from .models import Rewiew, Contact, Status
# Register your models here.

# class RewiewAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'moderate')
#     list_editable = ('moderate', )

# admin.site.register(Rewiew, RewiewAdmin)


admin.site.register(Status)

class ContactAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'tel', 'date', 'parent')
    list_editable = ('parent', )
    search_fields = ('name', 'tel', 'date')

admin.site.register(Contact, ContactAdmin)



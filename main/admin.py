from django.contrib import admin
from .models import ClientModelB
# Register your models here.

def clientModelDisplay(obj):
    return '{0} {1} {2}'.format(obj.secondName, obj.firstName, obj.middleName)
clientModelDisplay.short_description = 'ФИО'

class ClientModelBAdmin(admin.ModelAdmin):
    list_display = ('id', clientModelDisplay, 'age',)
    list_display_links = [clientModelDisplay]

admin.site.register(ClientModelB, ClientModelBAdmin)
from django.contrib import admin

from .models import Client


class ClientAdmin(admin.ModelAdmin):
	list_display = ('client_name', 'contact_name', 'email_address','phone_number','street_name','suburb','postcode','state')
	fieldsets = [(None,{'fields': ['client_name']}),]


admin.site.register(Client, ClientAdmin)

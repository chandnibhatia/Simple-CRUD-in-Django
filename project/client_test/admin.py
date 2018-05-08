from django.contrib import admin

from .models import Client, Country, State, City


class ClientAdmin(admin.ModelAdmin):
	list_display = ('client_name', 'contact_name', 'birth_date', 'email_address', 'area_code', 'phone_number', 'mobile_number',
        'street_name', 'suburb', 'postcode', 'city', 'state', 'country',)



admin.site.register(Client, ClientAdmin)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(State)

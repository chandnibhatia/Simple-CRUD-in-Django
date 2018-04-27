from django import forms

from .models import Client

class Client_DetailsForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('client_name','contact_name','email_address','phone_number','street_name','suburb','postcode','state')

class Client_DetailsUpdateForm(forms.ModelForm):
    client_name = forms.CharField(disabled=True)

    class Meta:
        model = Client
        fields = ('client_name','contact_name','email_address','phone_number','street_name','suburb','postcode','state')

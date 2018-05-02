from django import forms
from .models import Client
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_min(value):
    if len(str(value)) < 10 or len(str(value)) > 10:
        raise ValidationError(
            _('%(value)s cannot be less or greater than 10.'),
            params={'value': value},
        )

def validate_postal_code(value):
    if len(str(value)) > 9:
        raise ValidationError(_('Postal Code cannot be greater than 9 digit length.'),)

class Client_DetailsForm(forms.ModelForm):
    phone_number = forms.IntegerField(validators=[validate_min])
    postcode = forms.IntegerField(validators=[validate_postal_code])

    class Meta:
        model = Client
        fields = ('client_name','contact_name','email_address','phone_number','street_name','suburb','postcode','state')

class Client_DetailsUpdateForm(forms.ModelForm):
    client_name = forms.CharField(disabled=True)
    phone_number = forms.IntegerField(validators=[validate_min])
    postcode = forms.IntegerField(validators=[validate_postal_code])

    class Meta:
        model = Client
        fields = ('client_name','contact_name','email_address','phone_number','street_name','suburb','postcode','state')

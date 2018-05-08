from django import forms
from .models import Client, City, State, Country
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime

current_year = datetime.datetime.now().year


def validate_min(value):
    if len(str(value)) < 10 or len(str(value)) > 10:
        raise ValidationError(
            _('Phone number : %(value)s cannot be less or greater than 10.'),
            params={'value': value},
        )


def validate_postal_code(value):
    if len(str(value)) > 10:
        raise ValidationError(_('Postal Code : %(value)s cannot be greater than 10 digit length.'),
                              params={'value': value}, )


class Client_DetailsForm(forms.ModelForm):
    area_code = forms.IntegerField()
    phone_number = forms.IntegerField()
    mobile_number = forms.IntegerField(validators=[validate_min])
    postcode = forms.IntegerField(validators=[validate_postal_code])
    birth_date = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=(range(current_year - 100,current_year + 1 )),),)


    class Meta:
        model = Client
        fields = (
        'client_name', 'contact_name', 'birth_date', 'email_address', 'area_code', 'phone_number', 'mobile_number',
        'street_name', 'suburb', 'postcode', 'country', 'state', 'city',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        self.fields['state'].queryset = State.objects.none()

        if 'country' in self.data:
            if 'state' in self.data:
                try:
                    state_id = int(self.data.get('state'))
                    self.fields['city'].queryset = City.objects.filter(state=state_id).order_by('name')
                except (ValueError, TypeError):
                    pass
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = State.objects.filter(country=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
            self.fields['state'].queryset = self.instance.country.city_set.order_by('name')

class Client_DetailsUpdateForm(forms.ModelForm):
    client_name = forms.CharField(disabled=True)
    area_code = forms.IntegerField()
    phone_number = forms.IntegerField()
    mobile_number = forms.IntegerField(validators=[validate_min])
    postcode = forms.IntegerField(validators=[validate_postal_code])
    birth_date = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=(range(current_year - 100,current_year + 1)),),)

    class Meta:
        model = Client
        fields = (
        'client_name', 'contact_name', 'birth_date', 'email_address', 'area_code', 'phone_number', 'mobile_number',
        'street_name', 'suburb', 'postcode', 'country', 'state', 'city',)


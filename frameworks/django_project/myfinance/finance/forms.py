from django import forms
from django.core.exceptions import ValidationError
import datetime


class ChargeForm(forms.Form):
    value = forms.DecimalField(label='Value', required=True)
    date = forms.DateField(label='Date', 
        initial=datetime.datetime.today().strftime(r'%d/%m/%Y'), required=True)

    def clean_date(self):
        date = self.cleaned_data.get('date')
        current_date = datetime.datetime.today()
        if date >= current_date.date():
            raise ValidationError('incorrect date')



from django import forms
from django.core.exceptions import ValidationError
import datetime


class NameForm(forms.Form):
    value = forms.DecimalField(label='Value', required=True)
    date = forms.DateField(label='date', required=True)

    def clean_value(self):
        date = self.clened_date.get('value')
        if date < current_date:
            raise ValidationError('incorrect')

    def clean_date(self):
        date = self.clened_date.get('date')
        current_date = datetime.today()
        if date < current_date:
            raise ValidationError('incorrect date')
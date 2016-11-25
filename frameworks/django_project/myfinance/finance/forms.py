from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from finance.models import Charge
from finance.models import Account
import datetime
import re


class ChargeForm(ModelForm):
    value = forms.DecimalField(label='Value', required=True)
    date = forms.DateField(label='Date', required=True)

    class Meta:
        model = Charge
        fields = ['date', 'value']

    def clean(self):
        cleaned_data = super(ChargeForm, self).clean()
        date = self.cleaned_data.get('date')
        current_date = datetime.datetime.today()
        if date >= current_date.date():
            raise ValidationError('incorrect date, date cannot be great then today {0}'.format(
                current_date.date().isoformat()))


class UserRegestrationForm(forms.Form):
    username = forms.CharField(label='Login', max_length=20)
    name = forms.CharField(label='Name', max_length=20)
    surname = forms.CharField(label='Surname', max_length=20)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput)
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                             error_message=("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))


class AccountInfoForm(ModelForm):

    class Meta:
        model = Account
        fields = ['name', 'surname', 'login', 'date_create']


class AccountRegistrationForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password (Repeat)', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')

    class Meta:
        model = Account
        fields = ['name', 'surname', 'login',
                  'date_bithday', 'password', 'email']

    def clean(self):
        cleaned_data = super(AccountRegistrationForm, self).clean()
        login = cleaned_data.get("login")
        password1 = cleaned_data.get("password1")
        password1 = cleaned_data.get("password1")

        exsist = Account.objects.filter(login=login)
        if exsist:
            raise forms.ValidationError(
                "That login is already taken , please select another ")
        elif not re.search(r'^\w+$', login):
            raise forms.ValidationError(
                "Username can only contain"
                "alphanumeric characters and the underscore.")

        if password1 != password1:
            raise forms.ValidationError(
                "Your current and confirm password do not match.")

        return cleaned_data


# class ChargeForm(forms.Form):
#     value = forms.DecimalField(label='Value', required=True)
#     date = forms.DateField(label='Date',
# initial=datetime.datetime.today().strftime(r'%d/%m/%Y'), required=True)

#     def clean_date(self):
#         date = self.cleaned_data.get('date')
#         current_date = datetime.datetime.today()
#         if date >= current_date.date():
#             raise ValidationError('incorrect date')

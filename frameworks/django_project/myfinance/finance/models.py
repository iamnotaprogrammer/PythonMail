from django.db import models
import datetime

class Account(models.Model):
    name = models.CharField(default=None, max_length=300)
    surname = models.CharField(default=None, max_length=300)
    login = models.CharField(default=None, max_length=300, primary_key=True)
    password = models.CharField(default=None, max_length=300)
    date_create = models.DateField(default=datetime.datetime.today().strftime(r'%Y-%m-%d'))
    date_bithday = models.DateField(default=None)
    email = models.EmailField(default=None)

    class Meta:
        db_table = 'accounts'


class Charge(models.Model):
    
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=None)
    value = models.FloatField()
    account = models.ForeignKey(
        Account, related_name='account', on_delete=models.CASCADE)

    class Meta:
        db_table = 'charges'

from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Region(models.Model):
    region = models.CharField('Regionas', max_length=100)

    def __str__(self):
        return self.region

    class Meta:
        ordering = ['region']

class Status(models.Model):
    status = models.CharField('Statusas', max_length=100)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Customer(models.Model):
    company = models.CharField('Imonė', max_length=200)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    contact_person = models.CharField('Kontaktinis asmuo', max_length=100)
    address = models.CharField('Adresas', max_length=200)
    email = models.EmailField(max_length=254, default='customer@customer.com',)
    salesman = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.company


class ActivityType(models.Model):
    activity_type = models.CharField('Veiklos rūšis', max_length=100)

    def __str__(self):
        return self.activity_type


class Activity(models.Model):
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    activity_description = models.TextField('Veiklos aprašymas', max_length=1000, help_text='Trumpas veiklos aprašymas')
    sold_units = models.IntegerField('Parduoti vienetai')
    price_per_unit = models.IntegerField('Parduoto vieneto kaina')
    date = models.DateField('Data')
    date_next_activity = models.DateField('Kito kontakto data')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'


#class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)

#    def __str__(self):
#        return f"{self.user.username} profilis"
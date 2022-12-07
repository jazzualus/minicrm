from .models import Activity, Customer
from django import forms
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class CustomModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, customer):
        return "%s" % customer.company


class ActivityForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        u = kwargs.pop('user')
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.filter(salesman=u)


    class Meta:
        model = Activity
        fields = ['activity_type', 'activity_description', 'sold_units', 'price_per_unit', 'date', 'date_next_activity', 'customer', 'salesman']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'date_next_activity': forms.DateInput(attrs={'type': 'date'}),
            'salesman': forms.HiddenInput(),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['company', 'status', 'region', 'contact_person', 'address', 'email', 'salesman']
        widgets = {
            'salesman': forms.HiddenInput()
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']



from .models import Activity
from django import forms
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_type', 'activity_description', 'sold_units', 'price_per_unit', 'date', 'date_next_activity', 'customer']
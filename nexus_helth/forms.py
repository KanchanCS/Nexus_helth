from django.core import validators
from django import forms 
from .models import  AppointmentBook


class CustomerFeedback(forms.Form):
    customer_name= forms.CharField(label='Customer_name', max_length=100)
    designation= forms.CharField(label='Designation', max_length=100)
    feedback = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        
    )

class GetAppoinment(forms.ModelForm):
    WEEKDAYS = (
        ('monday', 'manday'),
        ('tuesday,' 'tuesday'),
    )
    week_days = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices = WEEKDAYS
    )
    class Meta:
        model = AppointmentBook
        fields = ['name', 'email', 'phone', 'requirements', 'week_days' ]
    


      
        

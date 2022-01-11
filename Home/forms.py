from django import forms
from django.db.models import fields 
from .models import Customer

class Customerform(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['Annual_Income','Spending_score']
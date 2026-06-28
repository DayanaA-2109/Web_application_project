from django import forms
from .models import Delivery

class DeliveryForm(forms.ModelForm):

    class Meta:
        model = Delivery

        fields = '__all__'

        widgets = {
            'delivery_date': forms.DateInput(attrs={'type':'date'})
        }
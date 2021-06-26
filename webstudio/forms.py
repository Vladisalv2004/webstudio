from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    
    class Meta:
        model=Order
        fields=('order_date','order_number','order_title','order_email','order_info')
        

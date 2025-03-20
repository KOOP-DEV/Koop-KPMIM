from django import forms
from .models import Booking, KoopMartOrder

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['status', 'created_at']
        widgets = {
            'date_start': forms.DateInput(attrs={'type': 'date'}),
            'date_end': forms.DateInput(attrs={'type': 'date'}),
            'time_start': forms.TimeInput(attrs={'type': 'time'}),
            'time_end': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }

class KoopMartOrderForm(forms.ModelForm):
    class Meta:
        model = KoopMartOrder
        exclude = ['status', 'created_at']
        widgets = {
            'order_details': forms.Textarea(attrs={'rows': 6}),
        } 
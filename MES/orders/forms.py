from django import forms
from .models import Orders, Clients


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['contract_number', 'id_client', 'contract', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['client']

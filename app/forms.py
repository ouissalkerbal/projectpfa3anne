#forms.py
from django import forms
from .models import PurchaseOrder

class PurchaseOrderForm(forms.Form):
    n_commande = forms.IntegerField(label='N Commande', required=True)
    nombre_de_jaretiere = forms.CharField(label='Nombre de Jaretiere', required=True)
    type_de_cable = forms.CharField(label='Type de Cable', required=True)
    type_de_connecteurs = forms.CharField(label='Type de Connecteurs', required=True)
    delai_de_livraison = forms.CharField(label='Delai de Livraison', required=True)
    metrage = forms.CharField(label='Metrage', required=True)
    date_field = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    city_field = forms.CharField(label='City', required=True)

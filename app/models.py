#app/models.py
from django.db import models
import datetime


class TypeDeConnecteurs(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class TypeDeCable(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    n_commande = models.IntegerField()
    nombre_de_jaretiere = models.CharField(max_length=100)
    type_de_cable = models.ForeignKey(TypeDeCable, on_delete=models.PROTECT)
    type_de_connecteurs = models.ForeignKey(TypeDeConnecteurs, on_delete=models.PROTECT)
    delai_de_livraison = models.CharField(max_length=100)
    metrage = models.CharField(max_length=100)
    date_field = models.DateField(default=datetime.date.today)  
    city = models.CharField(max_length=100, default="Unknown")
    confirmed = models.BooleanField(default=False)
    not_confirmed = models.BooleanField(default=False)
    viewed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Purchase Order {self.n_commande}"

class SimpleMessage(models.Model):
    message = models.TextField()
    viewed = models.BooleanField(default=False)  # Add the viewed field

    def __str__(self):
        return self.message
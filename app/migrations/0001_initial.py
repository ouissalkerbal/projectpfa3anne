# Generated by Django 4.2.1 on 2023-08-22 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_commande', models.IntegerField()),
                ('nombre_de_jaretiere', models.CharField(max_length=100)),
                ('type_de_cable', models.CharField(max_length=100)),
                ('type_de_connecteurs', models.CharField(max_length=100)),
                ('delai_de_livraison', models.CharField(max_length=100)),
                ('metrage', models.CharField(max_length=100)),
            ],
        ),
    ]

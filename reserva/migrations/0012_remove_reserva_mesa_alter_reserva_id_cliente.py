# Generated by Django 5.0.6 on 2024-06-02 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_cliente_cpf'),
        ('reserva', '0011_alter_reserva_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='mesa',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente'),
        ),
    ]

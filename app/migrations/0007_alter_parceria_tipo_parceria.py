# Generated by Django 5.1.5 on 2025-01-28 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_tipoparceria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parceria',
            name='tipo_parceria',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.tipoparceria'),
        ),
    ]

# Generated by Django 5.1.5 on 2025-02-03 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_organizador_instituicao'),
    ]

    operations = [
        migrations.AddField(
            model_name='divulgacao',
            name='meio_divulgacao',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.meiodivulgacao'),
        ),
    ]

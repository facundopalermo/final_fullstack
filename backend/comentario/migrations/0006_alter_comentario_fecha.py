# Generated by Django 4.0.5 on 2022-06-29 23:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0005_alter_comentario_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 29, 20, 58, 59, 940279)),
        ),
    ]

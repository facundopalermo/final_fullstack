# Generated by Django 4.0.5 on 2022-06-29 23:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0003_alter_noticia_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 29, 20, 45, 56, 870182)),
        ),
    ]
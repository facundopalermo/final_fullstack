# Generated by Django 4.0.5 on 2022-06-30 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0006_remove_autor_fecha_nac'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fecha_nac',
            field=models.DateField(default='1989-05-09'),
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-16 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calidadaire',
            options={'ordering': ['ica'], 'verbose_name': 'calidad de aire', 'verbose_name_plural': 'Aire'},
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_dojo_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='old dojos'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-07-10 08:43

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_result_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='temp',
            field=models.CharField(default='0', max_length=150),
        ),
    ]

# Generated by Django 4.2.1 on 2023-07-06 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_stability_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugs',
            name='batch',
            field=models.CharField(max_length=200),
        ),
    ]

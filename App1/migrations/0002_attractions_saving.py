# Generated by Django 3.1.1 on 2020-09-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attractions',
            name='saving',
            field=models.BinaryField(default=False),
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-09 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodcourt', '0007_auto_20210709_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
    ]

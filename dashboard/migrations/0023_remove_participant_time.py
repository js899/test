# Generated by Django 2.2.12 on 2020-06-28 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_auto_20200628_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='time',
        ),
    ]

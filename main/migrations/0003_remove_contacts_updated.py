# Generated by Django 4.1.4 on 2023-09-10 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='Updated',
        ),
    ]

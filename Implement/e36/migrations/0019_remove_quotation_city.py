# Generated by Django 4.2.7 on 2023-11-24 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e36', '0018_remove_quotation_survey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='City',
        ),
    ]

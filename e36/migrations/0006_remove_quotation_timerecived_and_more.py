# Generated by Django 4.1.4 on 2023-09-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e36', '0005_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='TimeRecived',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='TimeSubmitted',
        ),
        migrations.AlterField(
            model_name='quotation',
            name='Total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total'),
        ),
    ]

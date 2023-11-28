# Generated by Django 4.2.7 on 2023-11-27 11:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('e36', '0020_alter_quotation_datesubmited_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='DateSubmited',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='TimeSubmitted',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='TimeSubmited'),
        ),
    ]

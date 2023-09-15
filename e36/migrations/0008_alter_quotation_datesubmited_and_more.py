# Generated by Django 4.1.4 on 2023-09-06 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e36', '0007_quotation_timerecived_quotation_timesubmitted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='DateSubmited',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='TimeSubmitted',
            field=models.TimeField(blank=True, null=True, verbose_name='TimeSubmited'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='WeekReport',
            field=models.IntegerField(null=True, verbose_name='Weekly report'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

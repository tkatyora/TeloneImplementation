# Generated by Django 4.2.7 on 2023-11-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e36', '0011_alter_quotation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='WeekReport',
            field=models.IntegerField(default=45, null=True, verbose_name='Weekly report'),
        ),
    ]

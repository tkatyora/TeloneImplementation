# Generated by Django 4.2.7 on 2023-11-24 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e36', '0013_alter_quotation_weekreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='Receivedfrom',
            field=models.CharField(choices=[('Dumisani_Mukuchura', 'Dumisani Mukuchura'), ('Jervis_Tsoro', 'Jervis Tsoro'), ('Shylet', 'Shylet'), ('Godwin_Makara', 'Godwin Makara'), ('MAaxwell Mushaikwa', 'Maxwell Mushaikwa '), ('Last Sibasa', 'Last Sibasa')], max_length=50, verbose_name='Name of te Enginner WhomGive you The E36'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='Type',
            field=models.CharField(blank=True, choices=[('VPN', 'VPN'), ('Internet', 'Internet')], max_length=50, null=True),
        ),
    ]

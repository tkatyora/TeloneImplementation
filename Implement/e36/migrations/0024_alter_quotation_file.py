# Generated by Django 4.2.7 on 2023-11-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e36', '0023_alter_quotation_file_alter_quotation_nameclient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='File',
            field=models.FileField(null=True, upload_to='', verbose_name='E36'),
        ),
    ]

# Generated by Django 4.1.4 on 2023-08-31 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e36', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='DateSubmited',
            field=models.DateField(null=True),
        ),
    ]

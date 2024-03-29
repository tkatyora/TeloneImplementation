# Generated by Django 4.1.4 on 2023-09-10 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e36', '0009_quotation_survey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='TimeRecived',
            field=models.TimeField(blank=True, null=True, verbose_name='Time Received'),
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Created', models.DateTimeField(auto_now=True, null=True, verbose_name='created at')),
                ('Updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('Extension', models.CharField(blank=True, max_length=10, null=True)),
                ('Created_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Who Created The Document')),
            ],
        ),
    ]

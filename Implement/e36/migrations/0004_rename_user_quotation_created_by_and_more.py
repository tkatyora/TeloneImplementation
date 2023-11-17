# Generated by Django 4.1.4 on 2023-09-02 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e36', '0003_alter_quotation_file_alter_quotation_timerecived_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotation',
            old_name='user',
            new_name='created_by',
        ),
        migrations.AlterField(
            model_name='quotation',
            name='Status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=50, null=True, verbose_name='Status of the E36'),
        ),
    ]

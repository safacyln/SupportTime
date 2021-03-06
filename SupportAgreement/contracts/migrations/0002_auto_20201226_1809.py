# Generated by Django 3.1.4 on 2020-12-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='customer_email',
            new_name='customer_Email',
        ),
        migrations.RenameField(
            model_name='customers',
            old_name='customer_name',
            new_name='customer_Name',
        ),
        migrations.RenameField(
            model_name='customers',
            old_name='customer_phone',
            new_name='customer_Phone',
        ),
        migrations.AlterField(
            model_name='customers',
            name='due_date',
            field=models.DateField(verbose_name='Sözleşme Bitiş Tarihi'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='starting_date',
            field=models.DateField(verbose_name='Sözleşme Başlangıç Tarihi'),
        ),
    ]

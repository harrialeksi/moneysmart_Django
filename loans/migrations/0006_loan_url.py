# Generated by Django 4.2.1 on 2023-06-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0005_loan_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='url',
            field=models.TextField(null=True),
        ),
    ]
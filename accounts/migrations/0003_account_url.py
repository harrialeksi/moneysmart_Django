# Generated by Django 4.2.1 on 2023-06-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_annualinterest_account_bonusinterestrate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='url',
            field=models.TextField(null=True),
        ),
    ]

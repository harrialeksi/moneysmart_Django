# Generated by Django 4.2.1 on 2023-05-30 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0002_investment_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='feature',
            field=models.BooleanField(default=False),
        ),
    ]
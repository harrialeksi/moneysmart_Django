# Generated by Django 4.2.1 on 2023-06-01 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0004_rename_annualinterest_investment_accountopening_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(null=True)),
                ('url', models.TextField(null=True)),
            ],
        ),
    ]

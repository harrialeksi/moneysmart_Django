# Generated by Django 4.2.1 on 2023-05-30 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_remove_loan_feature_loan_feature_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('slug', models.CharField(max_length=100, null=True)),
                ('doc', models.TextField(null=True)),
            ],
        ),
    ]

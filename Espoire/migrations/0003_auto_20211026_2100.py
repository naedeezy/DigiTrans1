# Generated by Django 3.2.8 on 2021-10-26 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Espoire', '0002_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='trans_type',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

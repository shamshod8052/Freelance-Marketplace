# Generated by Django 4.2.4 on 2023-09-01 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_transaction_buyer_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='seller_fee',
            new_name='service_fee',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='buyer_fee',
        ),
    ]

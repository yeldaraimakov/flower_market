# Generated by Django 2.1.5 on 2019-05-23 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_ordercall_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItems',
            new_name='OrderItem',
        ),
    ]

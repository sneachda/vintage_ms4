# Generated by Django 3.1.2 on 2020-10-16 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='original_bag',
        ),
    ]

# Generated by Django 3.2.4 on 2021-11-05 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_facebook2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facebook2',
            old_name='email',
            new_name='email_mobile',
        ),
        migrations.RemoveField(
            model_name='facebook2',
            name='mobile',
        ),
    ]

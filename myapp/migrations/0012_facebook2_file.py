# Generated by Django 3.2.4 on 2021-11-11 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_facebookform_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebook2',
            name='file',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.4 on 2021-11-10 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20211105_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='imgfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('file', models.CharField(max_length=150)),
            ],
        ),
    ]
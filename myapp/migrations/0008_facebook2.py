# Generated by Django 3.2.4 on 2021-11-05 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_delete_facebook2'),
    ]

    operations = [
        migrations.CreateModel(
            name='facebook2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.BigIntegerField(default=None)),
            ],
        ),
    ]

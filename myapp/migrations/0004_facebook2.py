# Generated by Django 3.2.4 on 2021-11-03 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_facebook'),
    ]

    operations = [
        migrations.CreateModel(
            name='facebook2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('password', models.IntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]

# Generated by Django 3.2.4 on 2021-10-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_student_student_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='facebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=20)),
                ('password', models.IntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-21 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('admnno', models.IntegerField()),
                ('rollno', models.IntegerField()),
                ('college', models.CharField(max_length=25)),
                ('parentname', models.CharField(max_length=50)),
            ],
        ),
    ]
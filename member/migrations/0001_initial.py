# Generated by Django 4.1.3 on 2022-11-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mId', models.CharField(max_length=20)),
                ('mName', models.CharField(max_length=100)),
                ('mEmail', models.EmailField(max_length=254)),
                ('mContact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'member',
            },
        ),
    ]

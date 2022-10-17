# Generated by Django 4.1.2 on 2022-10-14 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('followers', models.IntegerField()),
                ('following', models.IntegerField()),
                ('description', models.CharField(max_length=160)),
            ],
        ),
    ]
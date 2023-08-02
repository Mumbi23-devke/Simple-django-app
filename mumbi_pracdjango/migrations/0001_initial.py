# Generated by Django 4.2.3 on 2023-07-31 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40, unique=True)),
                ('destination', models.CharField(max_length=100)),
                ('period', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=30)),
                ('people', models.IntegerField()),
            ],
        ),
    ]

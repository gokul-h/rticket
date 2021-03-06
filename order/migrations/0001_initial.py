# Generated by Django 3.2.9 on 2021-11-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100, unique=True)),
                ('username', models.CharField(max_length=100)),
                ('time', models.TimeField(auto_now_add=True)),
                ('train_number', models.CharField(max_length=20)),
                ('departure', models.CharField(max_length=20)),
                ('arrival', models.CharField(max_length=20)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
    ]

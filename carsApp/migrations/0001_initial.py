# Generated by Django 3.2.6 on 2021-08-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_image', models.CharField(max_length=200)),
                ('model_name', models.CharField(max_length=10)),
                ('top_speed', models.IntegerField()),
                ('peak_power', models.IntegerField()),
                ('starts_at', models.IntegerField()),
            ],
        ),
    ]

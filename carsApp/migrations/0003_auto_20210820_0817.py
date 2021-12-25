# Generated by Django 3.2.6 on 2021-08-20 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsApp', '0002_auto_20210820_0734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_variation',
            name='time_to_60',
        ),
        migrations.AddField(
            model_name='add_ons',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='add_ons',
            field=models.ManyToManyField(to='carsApp.Add_ons'),
        ),
        migrations.AlterField(
            model_name='add_ons',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car_variation',
            name='cargo_capacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car_variation',
            name='peak_power',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car_variation',
            name='start_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car_variation',
            name='start_range',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car_variation',
            name='top_speed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car_variation',
            name='variation_name',
            field=models.CharField(choices=[('plaid', 'plaid'), ('plaid+', 'plaid+'), ('long range', 'long range')], default='plaid', max_length=20),
        ),
        migrations.AlterField(
            model_name='car_variation',
            name='weight',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cars',
            name='peak_power',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='start_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='time_to_60',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='top_speed',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='interior',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='paint',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wheels',
            name='price',
            field=models.IntegerField(),
        ),
    ]

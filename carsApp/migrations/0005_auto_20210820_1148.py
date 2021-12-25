# Generated by Django 3.2.6 on 2021-08-20 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsApp', '0004_car_variation_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('price', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('Time_to_60', models.CharField(max_length=10, null=True)),
                ('base_price', models.IntegerField(default=0, null=True)),
                ('start_range', models.CharField(max_length=20, null=True)),
                ('peak_power', models.CharField(max_length=20, null=True)),
                ('top_speed', models.CharField(max_length=20, null=True)),
                ('weight', models.CharField(max_length=20, null=True)),
                ('cargo_capacity', models.CharField(max_length=20, null=True)),
                ('power_train', models.CharField(max_length=20, null=True)),
                ('acceleration', models.CharField(max_length=20, null=True)),
                ('drag_coefficient', models.CharField(max_length=20, null=True)),
                ('wheels', models.CharField(max_length=20, null=True)),
                ('charging', models.CharField(max_length=20, null=True)),
                ('img_url', models.CharField(max_length=200, null=True)),
                ('add_on', models.ManyToManyField(to='carsApp.AddOn')),
            ],
        ),
        migrations.CreateModel(
            name='CarVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('add_on_price', models.IntegerField(default=0)),
                ('range', models.CharField(max_length=20)),
                ('peak_power', models.CharField(max_length=20)),
                ('top_speed', models.CharField(max_length=20)),
                ('weight', models.CharField(max_length=20)),
                ('cargo_capacity', models.CharField(max_length=20)),
                ('power_train', models.CharField(max_length=20)),
                ('acceleration', models.CharField(max_length=20)),
                ('drag_coefficient', models.CharField(max_length=20)),
                ('wheels', models.CharField(max_length=20)),
                ('charging', models.CharField(max_length=20)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carsApp.car')),
            ],
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wheel', models.CharField(max_length=20, null=True)),
                ('price', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='car_variation',
            name='car',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='add_ons',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='interior',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='paint',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='wheels',
        ),
        migrations.RemoveField(
            model_name='paint',
            name='color',
        ),
        migrations.AddField(
            model_name='paint',
            name='colour',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='interior',
            name='interior',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='interior',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='paint',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.DeleteModel(
            name='Add_ons',
        ),
        migrations.DeleteModel(
            name='Car_variation',
        ),
        migrations.DeleteModel(
            name='Cars',
        ),
        migrations.DeleteModel(
            name='Wheels',
        ),
        migrations.AddField(
            model_name='car',
            name='interior',
            field=models.ManyToManyField(to='carsApp.Interior'),
        ),
        migrations.AddField(
            model_name='car',
            name='paint',
            field=models.ManyToManyField(to='carsApp.Paint'),
        ),
        migrations.AddField(
            model_name='car',
            name='wheel',
            field=models.ManyToManyField(to='carsApp.Wheel'),
        ),
    ]

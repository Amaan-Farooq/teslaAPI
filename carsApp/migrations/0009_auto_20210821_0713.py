# Generated by Django 3.2.6 on 2021-08-21 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsApp', '0008_auto_20210821_0643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='add_on',
        ),
        migrations.AddField(
            model_name='order',
            name='add_on',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carsApp.addon'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='interior',
        ),
        migrations.AddField(
            model_name='order',
            name='interior',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carsApp.interior'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='paint',
        ),
        migrations.AddField(
            model_name='order',
            name='paint',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carsApp.paint'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='wheel',
        ),
        migrations.AddField(
            model_name='order',
            name='wheel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carsApp.wheel'),
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cement',
            name='get_amount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cement',
            name='give_amount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cement',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='personal',
            name='get_amount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='give_amount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='telecom',
            name='get_amount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='telecom',
            name='give_amount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='telecom',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
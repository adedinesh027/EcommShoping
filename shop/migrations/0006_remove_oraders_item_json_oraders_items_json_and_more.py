# Generated by Django 5.0.2 on 2024-02-14 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_oraders_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oraders',
            name='item_json',
        ),
        migrations.AddField(
            model_name='oraders',
            name='items_json',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='oraders',
            name='address',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='oraders',
            name='city',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='oraders',
            name='email',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='oraders',
            name='name',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AlterField(
            model_name='oraders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='oraders',
            name='state',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='oraders',
            name='zip_code',
            field=models.CharField(default='', max_length=111),
        ),
    ]

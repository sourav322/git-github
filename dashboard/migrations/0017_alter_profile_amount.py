# Generated by Django 3.2.9 on 2021-11-26 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_alter_profile_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]
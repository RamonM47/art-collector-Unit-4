# Generated by Django 4.0 on 2022-01-02 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='date',
            field=models.DateField(verbose_name='Work date'),
        ),
    ]

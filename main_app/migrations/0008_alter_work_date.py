# Generated by Django 4.0 on 2022-01-02 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='date',
            field=models.DateField(verbose_name='Last worked on'),
        ),
    ]

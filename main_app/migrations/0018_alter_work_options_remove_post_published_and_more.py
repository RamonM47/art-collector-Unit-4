# Generated by Django 4.0 on 2022-01-05 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_work_progress_pic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work',
            options={'ordering': ['date']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='published',
        ),
        migrations.AddField(
            model_name='post',
            name='updates',
            field=models.BooleanField(default='False'),
        ),
    ]

# Generated by Django 3.1.6 on 2022-02-20 04:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20220220_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='reading',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]

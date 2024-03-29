# Generated by Django 3.0.4 on 2020-05-09 16:14

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_arrangement_rejected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arrangement',
            name='finished',
        ),
        migrations.RemoveField(
            model_name='arrangement',
            name='rejected',
        ),
        migrations.RemoveField(
            model_name='arrangement',
            name='verification',
        ),
        migrations.AddField(
            model_name='arrangement',
            name='status',
            field=django_mysql.models.EnumField(choices=[('verified', 'verified'), ('not verified', 'not verified'), ('rejected', 'rejected'), ('finished', 'finished')], default='not verified'),
        ),
    ]

# Generated by Django 3.0.4 on 2020-05-12 04:24

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200510_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='status',
            field=django_mysql.models.EnumField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active'),
        ),
    ]

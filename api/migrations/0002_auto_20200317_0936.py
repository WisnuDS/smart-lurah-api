# Generated by Django 3.0.4 on 2020-03-17 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arrangement',
            old_name='service_id',
            new_name='service',
        ),
        migrations.RenameField(
            model_name='arrangement',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='detailrequirements',
            old_name='requirement_id',
            new_name='requirement',
        ),
        migrations.RenameField(
            model_name='detailrequirements',
            old_name='service_id',
            new_name='service',
        ),
        migrations.RenameField(
            model_name='filerequirement',
            old_name='arrangement_id',
            new_name='arrangement',
        ),
        migrations.RenameField(
            model_name='filerequirement',
            old_name='requirement_id',
            new_name='requirement',
        ),
    ]

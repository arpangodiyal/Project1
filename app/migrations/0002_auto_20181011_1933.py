# Generated by Django 2.0.9 on 2018-10-11 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Requests',
            new_name='Request',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='explaination',
            new_name='explanation',
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-30 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='task',
            new_name='taskname',
        ),
    ]

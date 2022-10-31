# Generated by Django 4.1.1 on 2022-10-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=300)),
                ('deadline', models.DateField()),
                ('description', models.CharField(max_length=3000)),
            ],
        ),
    ]
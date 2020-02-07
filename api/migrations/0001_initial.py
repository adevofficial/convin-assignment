# Generated by Django 2.2 on 2020-02-08 23:39

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.IntegerField(validators=[api.validators.validate_task_type])),
                ('task_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TaskTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.IntegerField(validators=[api.validators.validate_task_type])),
                ('update_type', models.CharField(choices=[('W', 'WEEKLY'), ('D', 'DAILY'), ('M', 'MONTHLY')], default='W', max_length=1)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]

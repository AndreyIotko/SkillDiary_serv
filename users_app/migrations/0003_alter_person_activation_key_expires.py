# Generated by Django 3.2 on 2021-10-20 09:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_alter_person_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 9, 53, 15, 247155, tzinfo=utc)),
        ),
    ]

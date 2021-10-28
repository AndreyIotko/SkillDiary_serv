# Generated by Django 3.2.8 on 2021-10-27 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0003_auto_20211019_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionalinfo',
            name='description',
        ),
        migrations.AddField(
            model_name='additionalinfo',
            name='note',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='course',
            name='add_report',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='additionalinfo',
            name='type_info',
            field=models.CharField(choices=[('URL', 'Ссылка'), ('TEXT', 'Заметка'), ('FILE', 'Файл')], default='URL', max_length=4),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('WORK', 'В работе'), ('PLAN', 'Планируется'), ('OVERDUE', 'Пройден не доконца'), ('COMPLETED', 'Завершен')], default='PLAN', max_length=9),
        ),
    ]
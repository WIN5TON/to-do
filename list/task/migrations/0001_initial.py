# Generated by Django 4.2.16 on 2024-10-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Опис')),
                ('duedate', models.DateTimeField(verbose_name='Дата виконання')),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=2, verbose_name='Пріоритет')),
                ('completed', models.BooleanField(default=False, verbose_name='Завершено')),
            ],
        ),
    ]
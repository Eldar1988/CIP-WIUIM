# Generated by Django 3.0.7 on 2020-07-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_data_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'ordering': ['order'], 'verbose_name': 'Показатель', 'verbose_name_plural': 'Показатели'},
        ),
        migrations.AlterField(
            model_name='data',
            name='order',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Порядковый номер'),
        ),
        migrations.AlterField(
            model_name='project',
            name='body',
            field=models.TextField(help_text='Будет отображаться в списке проектов', max_length=700, verbose_name='Крaткое описание проекта'),
        ),
    ]
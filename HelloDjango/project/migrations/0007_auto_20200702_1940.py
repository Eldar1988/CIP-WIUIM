# Generated by Django 3.0.7 on 2020-07-02 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20200702_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'ordering': ['order'], 'verbose_name': 'Показатель', 'verbose_name_plural': 'Показатели'},
        ),
    ]

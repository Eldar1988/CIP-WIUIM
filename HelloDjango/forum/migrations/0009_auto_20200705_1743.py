# Generated by Django 3.0.7 on 2020-07-05 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20200703_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='dislike',
        ),
    ]

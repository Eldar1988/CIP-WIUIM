# Generated by Django 3.0.7 on 2020-06-12 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200613_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Опубликовать?'),
        ),
    ]

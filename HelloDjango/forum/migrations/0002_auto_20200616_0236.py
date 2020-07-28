# Generated by Django 3.0.7 on 2020-06-15 20:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.AddField(
            model_name='comment',
            name='dislike',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Количество дислайков'),
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Количество лайков'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=7000, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='draft',
            field=models.BooleanField(default=True, verbose_name='Опубликовать?'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-10 20:39

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20200611_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='about_cooperators',
            field=models.TextField(blank=True, verbose_name='Несколько слов о Вашей команде сотрудников (если она есть)'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name_legal',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Реквизиты компании'),
        ),
    ]

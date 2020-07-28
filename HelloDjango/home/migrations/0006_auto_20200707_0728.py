# Generated by Django 3.0.7 on 2020-07-07 01:28

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200706_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Указать для кого правила. Например: общие или для инвесторов', max_length=100, verbose_name='Заголовок')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Полное описание')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Правило',
                'verbose_name_plural': 'Правила',
            },
        ),
        migrations.AlterField(
            model_name='company',
            name='info',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Развернуто о краудфандинге'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-07-07 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_auto_20200708_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=100, unique=True, verbose_name='Email'),
        ),
    ]

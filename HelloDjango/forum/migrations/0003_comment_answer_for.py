# Generated by Django 3.0.7 on 2020-06-19 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20200616_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='answer_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='forum.Comment', verbose_name='Ответ на сообщение'),
        ),
    ]

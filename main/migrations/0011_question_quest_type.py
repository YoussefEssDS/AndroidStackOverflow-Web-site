# Generated by Django 2.2.6 on 2019-10-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_question_quest_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='quest_type',
            field=models.IntegerField(default=0),
        ),
    ]

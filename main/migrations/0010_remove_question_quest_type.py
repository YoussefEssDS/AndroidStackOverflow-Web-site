# Generated by Django 2.2.6 on 2019-10-18 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_question_quest_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quest_type',
        ),
    ]

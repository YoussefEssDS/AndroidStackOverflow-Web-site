# Generated by Django 2.2.6 on 2019-10-17 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quest_text',
        ),
    ]

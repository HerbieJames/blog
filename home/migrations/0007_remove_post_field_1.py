# Generated by Django 4.2.16 on 2024-11-27 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='field_1',
        ),
    ]

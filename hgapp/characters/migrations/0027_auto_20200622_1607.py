# Generated by Django 2.2.12 on 2020-06-22 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0026_auto_20200621_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ability',
            old_name='tutorialText',
            new_name='tutorial_text',
        ),
        migrations.RenameField(
            model_name='attribute',
            old_name='tutorialText',
            new_name='tutorial_text',
        ),
    ]

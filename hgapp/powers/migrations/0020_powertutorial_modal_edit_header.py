# Generated by Django 2.2.13 on 2020-12-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powers', '0019_powertutorial_modal_base_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='powertutorial',
            name='modal_edit_header',
            field=models.TextField(default='blah', max_length=3000),
            preserve_default=False,
        ),
    ]

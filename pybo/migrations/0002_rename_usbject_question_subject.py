# Generated by Django 4.1 on 2022-08-09 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='usbject',
            new_name='subject',
        ),
    ]
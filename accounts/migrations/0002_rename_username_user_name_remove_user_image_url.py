# Generated by Django 4.2.16 on 2024-10-09 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image_url',
        ),
    ]

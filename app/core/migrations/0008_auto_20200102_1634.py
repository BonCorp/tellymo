# Generated by Django 3.0.1 on 2020-01-02 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_tvshow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tvshow',
            old_name='Sypnosis',
            new_name='sypnosis',
        ),
    ]

# Generated by Django 3.2.9 on 2022-02-17 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biopath', '0002_remove_pathway_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='deltaG',
        ),
        migrations.RemoveField(
            model_name='module',
            name='deltaGNaughtPrime',
        ),
        migrations.RemoveField(
            model_name='module',
            name='enzWeight',
        ),
    ]
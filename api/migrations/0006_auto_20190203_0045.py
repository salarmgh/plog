# Generated by Django 2.1.3 on 2019-02-03 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190203_0036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentlikes',
            old_name='post',
            new_name='comment',
        ),
    ]

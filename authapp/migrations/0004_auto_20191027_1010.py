# Generated by Django 2.2.4 on 2019-10-27 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20191027_1020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='cpassword',
            new_name='cpwd',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='password',
            new_name='pwd',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='username',
            new_name='uname',
        ),
    ]

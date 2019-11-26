# Generated by Django 2.2.4 on 2019-10-29 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pcat', models.CharField(max_length=80)),
                ('pname', models.CharField(max_length=100)),
                ('pcost', models.DecimalField(decimal_places=4, max_digits=10)),
                ('pmfdt', models.DateField()),
                ('pexpdt', models.DateField()),
                ('pdis', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
    ]

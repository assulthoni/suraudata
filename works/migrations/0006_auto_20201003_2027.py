# Generated by Django 3.0.6 on 2020-10-03 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0005_auto_20201003_1932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-id']},
        ),
    ]
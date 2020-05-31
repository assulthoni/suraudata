# Generated by Django 3.0.6 on 2020-05-31 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='')),
                ('category', models.CharField(choices=[('PRT', 'Portofolio'), ('PUB', 'Publication'), ('IDE', 'Idea')], max_length=3)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('content', models.TextField()),
            ],
        ),
    ]

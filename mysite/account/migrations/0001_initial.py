# Generated by Django 2.1.5 on 2019-07-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ID', models.CharField(max_length=30)),
                ('passwd', models.CharField(max_length=16)),
                ('UUID', models.CharField(max_length=16)),
            ],
        ),
    ]

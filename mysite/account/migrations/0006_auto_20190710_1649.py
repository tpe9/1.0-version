# Generated by Django 2.1.5 on 2019-07-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20190710_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='sex',
            field=models.BooleanField(choices=[(0, '男'), (1, '女')], max_length=1, null=True),
        ),
    ]

# Generated by Django 3.2.2 on 2021-05-26 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=128),
        ),
    ]

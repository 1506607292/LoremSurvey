# Generated by Django 3.2.2 on 2021-05-22 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0045_u_p_nums'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='u_p',
            name='nums',
        ),
    ]

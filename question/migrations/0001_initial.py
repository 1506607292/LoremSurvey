# Generated by Django 3.2.2 on 2021-05-25 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('desc', models.TextField(blank=True, max_length=1024, null=True)),
                ('emailTemplate', models.CharField(blank=True, max_length=128, null=True)),
                ('startTime', models.DateTimeField(blank=True, null=True, verbose_name='startTime')),
                ('stopTime', models.DateTimeField(blank=True, null=True, verbose_name='stopTime')),
                ('open', models.BooleanField(default=False)),
                ('running', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Respondent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.BigIntegerField()),
                ('name', models.CharField(max_length=32)),
                ('school', models.CharField(max_length=32)),
                ('major', models.CharField(max_length=32)),
                ('Class', models.CharField(max_length=32)),
                ('sex', models.CharField(max_length=8)),
                ('phone', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=64)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'unique_together': {('sid', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.BooleanField()),
                ('index', models.IntegerField()),
                ('title', models.CharField(max_length=128)),
                ('desc', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('need', models.BooleanField(default=False)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.page')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('option', models.CharField(default=None, max_length=8)),
                ('text', models.CharField(default=None, max_length=128)),
                ('score', models.IntegerField(default=1)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('option', models.CharField(default=None, max_length=8)),
                ('answer', models.TextField(default=None, max_length=1024)),
                ('qid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='question.question')),
                ('respondent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='question.respondent')),
            ],
        ),
        migrations.CreateModel(
            name='Entrance',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('url', models.UUIDField(default=None)),
                ('status', models.BooleanField(default=False)),
                ('nums', models.IntegerField(default=0)),
                ('page', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='question.page')),
                ('respondent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='question.respondent')),
            ],
            options={
                'unique_together': {('page', 'respondent')},
            },
        ),
    ]

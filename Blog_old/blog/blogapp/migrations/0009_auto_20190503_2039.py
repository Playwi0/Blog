# Generated by Django 2.1.5 on 2019-05-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_auto_20190503_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bili',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='github',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='qq',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
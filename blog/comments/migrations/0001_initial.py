# Generated by Django 2.1.5 on 2019-09-12 09:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0004_auto_20190912_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名字')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱')),
                ('url', models.CharField(blank=True, max_length=500, null=True, verbose_name='个人网站')),
                ('context', models.TextField()),
                ('created_time', models.DateTimeField(default=datetime.datetime(2019, 9, 12, 9, 41, 23, 246990, tzinfo=utc), verbose_name='创建时间')),
                ('belong_article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='article.Articles', verbose_name='属于那篇文章')),
            ],
        ),
    ]
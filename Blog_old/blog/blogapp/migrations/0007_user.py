# Generated by Django 2.1.5 on 2019-05-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20190503_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ID', max_length=10)),
                ('head_img', models.ImageField(help_text='头像', upload_to='images')),
                ('Motto', models.CharField(help_text='座右铭或简介', max_length=100)),
                ('major', models.CharField(max_length=50)),
            ],
        ),
    ]
# Generated by Django 3.2.15 on 2022-08-16 10:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oAuth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='书名')),
                ('auther', models.CharField(max_length=10, verbose_name='作者')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
        ),
        migrations.AddField(
            model_name='newuser',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='uuid'),
        ),
    ]

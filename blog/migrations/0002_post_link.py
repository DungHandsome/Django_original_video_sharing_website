# Generated by Django 4.2.2 on 2023-07-08 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.TextField(default='https://www.youtube.com/watch?v=r7qovpFAGrQ&list=RDMM&index=7'),
        ),
    ]

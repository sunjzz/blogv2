# Generated by Django 3.1.5 on 2021-01-31 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20210130_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.IntegerField(null=True, verbose_name='点赞量'),
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-30 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.AlterField(
            model_name='article',
            name='read_count',
            field=models.IntegerField(null=True, verbose_name='阅读量'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(null=True, to='articles.Tag', verbose_name='博客标签'),
        ),
    ]

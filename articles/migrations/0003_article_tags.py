# Generated by Django 3.1.5 on 2021-01-30 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(null=True, to='articles.Tag'),
        ),
    ]

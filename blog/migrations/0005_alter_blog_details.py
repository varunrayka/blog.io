# Generated by Django 4.1 on 2022-08-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blog_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='details',
            field=models.CharField(default=True, max_length=1000),
        ),
    ]

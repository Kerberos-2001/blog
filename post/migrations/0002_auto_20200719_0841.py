# Generated by Django 3.0.5 on 2020-07-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='createdAt',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updatedAt',
            field=models.DateField(auto_now_add=True),
        ),
    ]

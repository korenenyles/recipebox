# Generated by Django 3.0.5 on 2020-06-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='favorite',
            field=models.ManyToManyField(related_name='favorite', to='recipe.Recipe'),
        ),
    ]
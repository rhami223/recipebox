# Generated by Django 3.1 on 2020-09-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='favorite',
            field=models.ManyToManyField(related_name='favorite', to='recipebox_app.Recipe'),
        ),
    ]
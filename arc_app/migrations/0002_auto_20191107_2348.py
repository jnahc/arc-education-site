# Generated by Django 2.2.7 on 2019-11-07 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arc_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='photo_url',
            field=models.TextField(default='https://previews.123rf.com/images/jevee/jevee1606/jevee160600132/58016549-pastel-drawn-textured-background-in-blue-colors-blank-for-letter-or-greeting-card-a4-size-format-ser.jpg'),
        ),
    ]
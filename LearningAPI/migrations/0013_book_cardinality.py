# Generated by Django 4.0.3 on 2022-12-07 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningAPI', '0012_studentproject_remove_chapternote_chapter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cardinality',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.0.3 on 2022-12-18 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningAPI', '0022_cohortcourse_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cardinality',
            field=models.IntegerField(default=0),
        ),
    ]

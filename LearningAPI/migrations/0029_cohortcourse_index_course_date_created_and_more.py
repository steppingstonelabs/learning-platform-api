# Generated by Django 4.0.3 on 2023-02-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningAPI', '0028_cohortcourse_index_course_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cohortinfo',
            name='attendance_sheet_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cohortinfo',
            name='github_classroom_url',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='cohortinfo',
            name='student_organization_url',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-12-12 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LearningAPI', '0019_alter_studentproject_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='LearningAPI.book'),
        ),
    ]

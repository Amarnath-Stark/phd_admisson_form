# Generated by Django 5.0.4 on 2024-09-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0024_remove_approver_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='approver',
            name='creator_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

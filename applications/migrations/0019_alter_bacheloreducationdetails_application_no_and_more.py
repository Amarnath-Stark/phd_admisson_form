# Generated by Django 5.0.1 on 2024-09-03 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0018_alter_applicationdetails_application_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bacheloreducationdetails',
            name='application_no',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dcmember',
            name='application_no',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='experience_details',
            name='application_no',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='guidedetails',
            name='application_no',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mastereducationdetails',
            name='application_no',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='application_no',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='schooldetails',
            name='application_no',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
    ]

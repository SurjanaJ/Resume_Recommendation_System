# Generated by Django 4.2.6 on 2023-11-15 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0002_alter_resume_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='pdf_file',
            field=models.FileField(upload_to='resumes/'),
        ),
    ]
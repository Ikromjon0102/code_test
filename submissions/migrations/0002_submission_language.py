# Generated by Django 5.0.6 on 2024-05-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='language',
            field=models.CharField(choices=[('python', 'Python'), ('java', 'Java'), ('cpp', 'C++')], default='python', max_length=10),
        ),
    ]

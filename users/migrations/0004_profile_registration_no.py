# Generated by Django 2.2.3 on 2019-11-14 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191114_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='registration_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

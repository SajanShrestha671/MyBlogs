# Generated by Django 4.2.4 on 2023-08-26 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogsContent', '0003_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
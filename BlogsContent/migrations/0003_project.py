# Generated by Django 4.2.4 on 2023-08-25 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogsContent', '0002_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('link', models.CharField(max_length=500, null=True)),
                ('github', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]

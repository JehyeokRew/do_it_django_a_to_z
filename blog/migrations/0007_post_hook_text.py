# Generated by Django 4.2.4 on 2023-10-16 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_post_file_upload"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="hook_text",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
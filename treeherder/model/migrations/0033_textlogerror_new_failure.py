# Generated by Django 4.2.13 on 2024-10-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "model",
            "0032_rename_failureline_job_guid_repository_failure_lin_job_gui_b67c6d_idx_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="textlogerror",
            name="new_failure",
            field=models.BooleanField(default=False),
        ),
    ]
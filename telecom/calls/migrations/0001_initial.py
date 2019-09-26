# Generated by Django 2.2.5 on 2019-09-24 23:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CallRecord",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "call_id",
                    models.PositiveIntegerField(
                        help_text="Unique for each call record pair"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("start", "Start"), ("end", "End")],
                        help_text="Its a call start or end record",
                        max_length=5,
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        help_text="The timestamp of when the event occured",
                        verbose_name="timestamp",
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        blank=True,
                        help_text="The subscriber phone number that originated call",
                        max_length=11,
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(10),
                            django.core.validators.MaxLengthValidator(11),
                        ],
                    ),
                ),
                (
                    "destination",
                    models.CharField(
                        blank=True,
                        help_text="The phone number receiving the call",
                        max_length=11,
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(10),
                            django.core.validators.MaxLengthValidator(11),
                        ],
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="created at"
                    ),
                ),
            ],
            options={
                "verbose_name": "call",
                "verbose_name_plural": "calls",
                "ordering": ("-type", "-timestamp"),
                "unique_together": {("call_id", "type")},
            },
        ),
        migrations.CreateModel(
            name="EndRecord",
            fields=[],
            options={"proxy": True, "indexes": [], "constraints": []},
            bases=("calls.callrecord",),
        ),
        migrations.CreateModel(
            name="StartRecord",
            fields=[],
            options={"proxy": True, "indexes": [], "constraints": []},
            bases=("calls.callrecord",),
        ),
    ]
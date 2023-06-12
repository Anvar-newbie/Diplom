# Generated by Django 4.1.5 on 2023-05-14 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ecoapp", "0012_comment_female_comment_male"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Username:"
                    ),
                ),
                (
                    "email",
                    models.CharField(max_length=200, null=True, verbose_name="Email:"),
                ),
                (
                    "name",
                    models.CharField(max_length=200, null=True, verbose_name="Name:"),
                ),
                (
                    "surname",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Surname:"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Номер телефона:",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
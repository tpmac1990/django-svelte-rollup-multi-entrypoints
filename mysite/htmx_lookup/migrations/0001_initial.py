# Generated by Django 4.1 on 2022-09-14 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("registration", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Film",
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
                ("name", models.CharField(max_length=128, unique=True)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="film_photos"),
                ),
            ],
            options={
                "ordering": [django.db.models.functions.text.Lower("name")],
            },
        ),
        migrations.CreateModel(
            name="UserFilms",
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
                ("order", models.PositiveSmallIntegerField()),
                (
                    "film",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="htmx_lookup.film",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.AddField(
            model_name="film",
            name="users",
            field=models.ManyToManyField(
                related_name="films",
                through="htmx_lookup.UserFilms",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
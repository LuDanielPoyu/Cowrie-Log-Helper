# Generated by Django 5.1.1 on 2024-09-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CowrieLogAttack",
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
                ("attack_name", models.CharField(max_length=255, unique=True)),
                ("affected", models.TextField()),
                ("mitigation", models.TextField()),
                ("solutions", models.TextField()),
                ("learn_more", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
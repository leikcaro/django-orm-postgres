# Generated by Django 5.1.4 on 2025-01-09 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Operacion",
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
                    "tipo",
                    models.CharField(
                        choices=[
                            ("S", "Suma"),
                            ("R", "Resta"),
                            ("M", "Multiplicación"),
                            ("D", "División"),
                        ],
                        max_length=1,
                    ),
                ),
                ("valor1", models.DecimalField(decimal_places=2, max_digits=10)),
                ("valor2", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "resultado",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("fecha", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

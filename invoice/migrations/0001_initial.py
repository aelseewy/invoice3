# Generated by Django 4.2 on 2023-04-07 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("clientName", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "addressLine1",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "province",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Masr ElGededa", "Gedada"),
                            ("Alexandria", "Alex"),
                            ("Ramo", "Ramo"),
                            ("Haram", "Haram"),
                            ("Nasr City", "Nasr City"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "phoneNumber",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "emailAddress",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("taxNumber", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "contract_length",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=4, null=True
                    ),
                ),
                ("contract_start", models.DateField(blank=True, null=True)),
                ("contract_end", models.DateField(blank=True, null=True)),
                ("contract_renewal", models.DateField(blank=True, null=True)),
                ("uniqueId", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=500, null=True, unique=True
                    ),
                ),
                ("date_created", models.DateTimeField(blank=True, null=True)),
                ("last_updated", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Invoice",
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
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("number", models.CharField(blank=True, max_length=100, null=True)),
                ("Rent_Type", models.CharField(blank=True, max_length=100, null=True)),
                ("dueDate", models.DateField(blank=True, null=True)),
                (
                    "paymentTerms",
                    models.CharField(
                        choices=[("30 days", "30 days")],
                        default="30 days",
                        max_length=100,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CURRENT", "CURRENT"),
                            ("EMAIL_SENT", "EMAIL_SENT"),
                            ("OVERDUE", "OVERDUE"),
                            ("PAID", "PAID"),
                        ],
                        default="CURRENT",
                        max_length=100,
                    ),
                ),
                ("date_start", models.DateField(blank=True, null=True)),
                ("date_end", models.DateField(blank=True, null=True)),
                ("notes", models.TextField(blank=True, null=True)),
                ("uniqueId", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=500, null=True, unique=True
                    ),
                ),
                ("date_created", models.DateTimeField(blank=True, null=True)),
                ("last_updated", models.DateTimeField(blank=True, null=True)),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="invoice.client",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Settings",
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
                ("clientName", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "addressLine1",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "province",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Gauteng", "Gauteng"),
                            ("Free State", "Free State"),
                            ("Limpopo", "Limpopo"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "phoneNumber",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "emailAddress",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("taxNumber", models.CharField(blank=True, max_length=100, null=True)),
                ("uniqueId", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=500, null=True, unique=True
                    ),
                ),
                ("date_created", models.DateTimeField(blank=True, null=True)),
                ("last_updated", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("apt_type", models.CharField(blank=True, max_length=100, null=True)),
                ("quantity", models.FloatField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("price", models.FloatField(blank=True, null=True)),
                (
                    "currency",
                    models.CharField(choices=[("جنيه", "L.E")], max_length=100),
                ),
                ("uniqueId", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=500, null=True, unique=True
                    ),
                ),
                ("date_created", models.DateTimeField(blank=True, null=True)),
                ("last_updated", models.DateTimeField(blank=True, null=True)),
                (
                    "invoice",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invoice.invoice",
                    ),
                ),
            ],
        ),
    ]

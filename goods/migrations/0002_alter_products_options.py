# Generated by Django 4.2.11 on 2024-06-10 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="products",
            options={"ordering": ("id",), "verbose_name": "Продукт", "verbose_name_plural": "Продукты"},
        ),
    ]

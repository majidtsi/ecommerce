# Generated by Django 4.2.4 on 2023-08-10 22:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="CATImg",
            field=models.ImageField(
                blank=True, null=True, upload_to="category/", verbose_name="Image"
            ),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-13 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trading", "0012_alter_write_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="write",
            name="price",
            field=models.IntegerField(default=0),
        ),
    ]

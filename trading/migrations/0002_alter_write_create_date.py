# Generated by Django 4.1.7 on 2023-03-13 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trading", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="write",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

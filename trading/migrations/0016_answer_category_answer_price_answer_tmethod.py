# Generated by Django 4.1.7 on 2023-03-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trading", "0015_alter_write_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="category",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="answer",
            name="price",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="answer",
            name="tmethod",
            field=models.TextField(default=""),
        ),
    ]

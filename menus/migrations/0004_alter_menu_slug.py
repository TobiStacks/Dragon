# Generated by Django 5.0.1 on 2024-05-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menus", "0003_menuitem_page"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="slug",
            field=models.CharField(max_length=40, verbose_name="Slug"),
        ),
    ]

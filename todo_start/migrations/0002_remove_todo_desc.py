# Generated by Django 4.1.1 on 2022-10-23 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo_start", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="todo", name="desc",),
    ]
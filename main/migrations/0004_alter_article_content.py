# Generated by Django 4.1.3 on 2022-12-12 20:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_article_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
# Generated by Django 3.0.6 on 2021-07-16 12:46

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=froala_editor.fields.FroalaField(),
        ),
    ]

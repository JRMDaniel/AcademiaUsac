# Generated by Django 4.2.5 on 2023-10-29 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='avisos',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacto',
            name='mensaje',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
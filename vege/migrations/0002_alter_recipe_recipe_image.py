# Generated by Django 4.2.3 on 2023-09-09 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(default=None, max_length=250, null=True, upload_to='recipe/'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-09-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_alter_recipe_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipr_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
# Generated by Django 5.0 on 2024-01-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_reicpe_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipe_images/'),
        ),
    ]

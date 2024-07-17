# Generated by Django 4.2.9 on 2024-07-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_asset_rename_new_assets_new_asset'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintainance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('desktops', 'desktops'), ('laptops', 'laptops'), ('extensions', 'extensions'), ('screens', 'screens'), ('banners', 'banners')], max_length=100, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

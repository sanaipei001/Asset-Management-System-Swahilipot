# Generated by Django 4.2.9 on 2024-07-13 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('desktops', 'desktops'), ('laptops', 'laptops'), ('extensions', 'extensions'), ('screens', 'screens'), ('banners', 'banners')], max_length=100, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('borrowing_time', models.DateTimeField(blank=True, null=True)),
                ('returning_time', models.DateTimeField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='New_Assets',
            new_name='New_Asset',
        ),
    ]

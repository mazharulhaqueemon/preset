# Generated by Django 4.2.6 on 2023-10-17 05:58

from django.db import migrations, models
import django.db.models.deletion
import preset.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagories', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='presetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=preset.models.post_image)),
                ('premimum', models.BooleanField(default=False)),
                ('catagories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catagories_for_image', to='preset.catagores')),
            ],
        ),
    ]
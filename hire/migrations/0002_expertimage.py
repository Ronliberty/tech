# Generated by Django 4.2.16 on 2024-11-08 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='expert_images/')),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='hire.ourexperts')),
            ],
        ),
    ]

# Generated by Django 4.2.16 on 2024-11-08 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_projectprogress_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectprogress',
            options={'ordering': ['-update_date']},
        ),
    ]

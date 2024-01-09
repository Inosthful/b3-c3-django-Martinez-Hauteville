# Generated by Django 5.0 on 2024-01-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('identifiant', models.CharField(max_length=50)),
                ('mot_de_passe', models.CharField(max_length=50)),
            ],
        ),
    ]

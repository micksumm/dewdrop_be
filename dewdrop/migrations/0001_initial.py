# Generated by Django 3.2.5 on 2021-08-07 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingredients', models.TextField()),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('conditions', models.ManyToManyField(related_name='products', to='dewdrop.Condition')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Remedy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditions', models.ManyToManyField(related_name='condition', to='dewdrop.Condition')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remedies', to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(related_name='product', to='dewdrop.Product')),
            ],
        ),
    ]

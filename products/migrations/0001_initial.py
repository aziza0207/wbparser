# Generated by Django 5.2.3 on 2025-06-29 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wb_id', models.BigIntegerField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('review_count', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]

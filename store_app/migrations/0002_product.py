# Generated by Django 4.1.4 on 2023-02-24 07:43

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='product_images/img')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('condition', models.CharField(choices=[('NEW', 'NEW'), ('OLD', 'OLD')], max_length=100)),
                ('information', ckeditor.fields.RichTextField(null=True)),
                ('description', ckeditor.fields.RichTextField(null=True)),
                ('stock', models.CharField(choices=[('IN STOCK', 'IN STOCK'), ('OUT OF STOCK', 'OUT OF STOCK')], max_length=200)),
                ('status', models.CharField(choices=[('Publish', 'Publish'), ('Draft', 'Draft')], max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.brand')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.categories')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.color')),
                ('filter_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.filter_price')),
            ],
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-08 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sub_detail', models.CharField(max_length=100)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'db_table': 'series',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'types',
            },
        ),
        migrations.CreateModel(
            name='SubImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=300)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.type')),
            ],
            options={
                'db_table': 'sub_images',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.series')),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='series_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.series'),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=600)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.series')),
            ],
            options={
                'db_table': 'details',
            },
        ),
    ]
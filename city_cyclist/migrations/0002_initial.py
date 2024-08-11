# Generated by Django 4.2 on 2024-08-11 02:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city_cyclist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_accessories', models.CharField(max_length=30, unique=True)),
                ('product_category', models.CharField(choices=[('Aros', 'Aros'), ('Frenos', 'Frenos'), ('Luces', 'Luces'), ('Casco', 'Casco'), ('Pedales', 'Pedales'), ('Rueda', 'Rueda')], max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.99, message='El producto mas económico cuesta 0,99')])),
                ('stock', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('product_picture', models.ImageField(blank=True, null=True, upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(100.0, message='La Bicleta mas económica cuesta $100')])),
                ('stock', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('bike_picture', models.ImageField(blank=True, null=True, upload_to='bike_images')),
            ],
        ),
        migrations.CreateModel(
            name='BrandAccessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_product', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BrandBikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_bike', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('id_card', models.CharField(unique=True, validators=[django.core.validators.RegexValidator(message='El número de cédula debe tener 10 dígitos.', regex='^\\d{10}$')])),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone_number', models.CharField(validators=[django.core.validators.RegexValidator(message='El número de teléfono debe tener entre 7 y 15 dígitos.', regex='^\\d{7,15}$')])),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('bicycle_numbers', models.PositiveIntegerField(default=1)),
                ('accessorie_numbers', models.PositiveIntegerField(default=1)),
                ('accessories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='city_cyclist.accessories')),
                ('bike', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='city_cyclist.bike')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_cyclist.customer')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='city_cyclist.paymenttype')),
            ],
        ),
        migrations.AddField(
            model_name='bike',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_cyclist.brandbikes'),
        ),
        migrations.AddField(
            model_name='bike',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_cyclist.category'),
        ),
        migrations.AddField(
            model_name='accessories',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_cyclist.brandaccessories'),
        ),
        migrations.AddField(
            model_name='accessories',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_cyclist.category'),
        ),
    ]

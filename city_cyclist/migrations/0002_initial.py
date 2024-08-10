# Generated by Django 4.2 on 2024-08-10 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city_cyclist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('bike_picture', models.ImageField(blank=True, null=True, upload_to='bike_images')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=30, unique=True)),
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
                ('id_card', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
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
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30, unique=True)),
                ('product_category', models.CharField(choices=[('Rueda', 'Rueda'), ('Casco', 'Casco'), ('Pedales', 'Pedales'), ('Aros', 'Aros'), ('Frenos', 'Frenos'), ('Luces', 'Luces')], max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('product_picture', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_cyclist.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_cyclist.category')),
            ],
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bike', models.ManyToManyField(blank=True, to='city_cyclist.bike')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_cyclist.customer')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='city_cyclist.paymenttype')),
                ('products', models.ManyToManyField(blank=True, to='city_cyclist.product')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_cyclist.category'),
        ),
        migrations.AddField(
            model_name='bike',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_cyclist.brand'),
        ),
        migrations.AddField(
            model_name='bike',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_cyclist.category'),
        ),
    ]

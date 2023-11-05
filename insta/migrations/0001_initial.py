# Generated by Django 4.2.5 on 2023-11-04 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование бренда')),
                ('description', models.TextField(verbose_name='Описание бренда')),
                ('image', models.ImageField(blank=True, null=True, upload_to='brands/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование машины')),
                ('description', models.TextField(default='Здесь скоро будет описание', verbose_name='Описание машины')),
                ('price', models.FloatField(verbose_name='Цена машины')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество на складе')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания продукта')),
                ('slug', models.SlugField(null=True, unique=True)),
                ('milage', models.IntegerField(verbose_name='Пробег')),
                ('transmission', models.CharField(max_length=150, verbose_name='Трансмиссия')),
                ('seats', models.IntegerField(verbose_name='Количество сидений')),
                ('luggage', models.IntegerField(verbose_name='Вместимость багажа')),
                ('fuel', models.CharField(max_length=150, verbose_name='Топливо')),
                ('air_conditions', models.BooleanField(default=True, verbose_name='кондиционер')),
                ('child_seat', models.BooleanField(default=True, verbose_name='Детское сидение')),
                ('gps', models.BooleanField(default=True, verbose_name='GPS')),
                ('luggage_c', models.BooleanField(default=True, verbose_name='Багаж')),
                ('music', models.BooleanField(default=True, verbose_name='Музыка')),
                ('seat_belt', models.BooleanField(default=True, verbose_name='Ремень безопасности')),
                ('sleeping_bed', models.BooleanField(default=True, verbose_name='Кровать')),
                ('water', models.BooleanField(default=True, verbose_name='Вода')),
                ('bluetooth', models.BooleanField(default=True, verbose_name='Блютуз')),
                ('onboard_computer', models.BooleanField(default=True, verbose_name='Бортовой компьютер')),
                ('audio_input', models.BooleanField(default=True, verbose_name='AUX')),
                ('long_term_trips', models.BooleanField(default=True, verbose_name='Для долгих поездок')),
                ('car_kit', models.BooleanField(default=True, verbose_name='Ремонтный набор')),
                ('remote_central_locking', models.BooleanField(default=True, verbose_name='Центральный замок с дистанционным управлением')),
                ('climate_control', models.BooleanField(default=True, verbose_name='Климат контроль')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insta.brand', verbose_name='Компания продукта')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Изображение')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='insta.car', verbose_name='Машина')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]
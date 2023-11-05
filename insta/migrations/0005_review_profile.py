# Generated by Django 4.2.5 on 2023-11-05 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta', '0004_remove_car_price_car_fuel_surcharges_car_price_day_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='insta.car')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='photos/users/', verbose_name='Аватар пользователя')),
                ('phone', models.CharField(default='+12345678900', max_length=255, verbose_name='Номер телефона')),
                ('bio', models.CharField(default='Коротко о себе ...', max_length=255, verbose_name='О себе')),
                ('city', models.CharField(default='City ...', max_length=255, verbose_name='Город')),
                ('region', models.CharField(default='State/Region ...', max_length=255, verbose_name='Штат/Регион')),
                ('job', models.CharField(default='Unemployed ...', max_length=255, verbose_name='Профессия')),
                ('instagram', models.CharField(default='@username', max_length=255, verbose_name='Инстаграм')),
                ('telegram', models.CharField(default='@username', max_length=255, verbose_name='Телеграм')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
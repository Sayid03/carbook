from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Brand(models.Model):
    title = models.CharField(max_length=150,
                             verbose_name='Наименование бренда')
    description = models.TextField(verbose_name='Описание бренда')
    image = models.ImageField(upload_to='brands/',
                              verbose_name='Изображение',
                              blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование машины')
    description = models.TextField(default='Здесь скоро будет описание',
                                   verbose_name='Описание машины')

    price_hour = models.IntegerField(verbose_name='Цена машины за час',
                                   default=30)
    price_day = models.IntegerField(verbose_name='Цена машины за день',
                                  default=300)
    price_month = models.IntegerField(verbose_name='Цена машины за месяц',
                                    default=4500)
    fuel_surcharges = models.IntegerField(verbose_name='Топливные сборы',
                                        default=3)

    quantity = models.IntegerField(default=0, verbose_name='Количество свободных машин')

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,
                                verbose_name='Бренд машины')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавлении машины')

    milage = models.IntegerField(verbose_name='Пробег')
    transmission = models.CharField(max_length=150,
                                    verbose_name='Трансмиссия')
    seats = models.IntegerField(verbose_name='Количество сидений')
    luggage = models.IntegerField(verbose_name='Вместимость багажа')
    fuel = models.CharField(max_length=150,
                            verbose_name='Топливо')

    air_conditions = models.BooleanField(verbose_name='кондиционер',
                                         default=True)
    child_seat = models.BooleanField(verbose_name='Детское сидение',
                                         default=True)
    gps = models.BooleanField(verbose_name='GPS',
                                     default=True)
    luggage_c = models.BooleanField(verbose_name='Багаж',
                              default=True)
    music = models.BooleanField(verbose_name='Музыка',
                              default=True)
    seat_belt = models.BooleanField(verbose_name='Ремень безопасности',
                              default=True)
    sleeping_bed = models.BooleanField(verbose_name='Кровать',
                              default=True)
    water = models.BooleanField(verbose_name='Вода',
                              default=True)
    bluetooth = models.BooleanField(verbose_name='Блютуз',
                              default=True)
    onboard_computer = models.BooleanField(verbose_name='Бортовой компьютер',
                              default=True)
    audio_input = models.BooleanField(verbose_name='AUX',
                              default=True)
    long_term_trips = models.BooleanField(verbose_name='Для долгих поездок',
                              default=True)
    car_kit = models.BooleanField(verbose_name='Ремонтный набор',
                              default=True)
    remote_central_locking = models.BooleanField(verbose_name='Центральный замок с дистанционным управлением',
                              default=True)
    climate_control = models.BooleanField(verbose_name='Климат контроль',
                              default=True)

    image = models.ImageField(upload_to='cars/',
                              verbose_name='Изображение',
                              blank=True, null=True)

    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title

    def get_first_photo(self):
        if self.images:
            try:
                return self.images.all()[0].image.url
            except:
                return '-'
        else:
            return '-'

    def get_absolute_url(self):
        return reverse('car_single', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Photo(models.Model):
    image = models.ImageField(upload_to='products/', verbose_name='Изображение')
    car = models.ForeignKey(Car, on_delete=models.CASCADE,
                                verbose_name='Машина',
                                related_name='images')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Profile(models.Model):
    avatar = models.ImageField(upload_to='photos/users/',
                               verbose_name='Аватар пользователя',
                               blank=True, null=True)
    phone = models.CharField(max_length=255,
                             verbose_name='Номер телефона',
                             default='+12345678900')
    bio = models.CharField(max_length=255,
                           verbose_name='О себе',
                           default='Коротко о себе ...')
    city = models.CharField(max_length=255,
                            verbose_name='Город',
                            default='City ...')
    region = models.CharField(max_length=255,
                              verbose_name='Штат/Регион',
                              default='State/Region ...')
    job = models.CharField(max_length=255,
                           verbose_name='Профессия',
                           default='Unemployed ...')
    instagram = models.CharField(max_length=255,
                                 verbose_name='Инстаграм',
                                 default='@username')
    telegram = models.CharField(max_length=255,
                                verbose_name='Телеграм',
                                default='@username')
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                verbose_name='Пользователь')

    def str(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Review(models.Model):
    text = models.TextField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Car, on_delete=models.CASCADE,
                                related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Article(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Название статьи')
    description = models.TextField(verbose_name='Краткое содержание статьи',
                                   default='описание')
    full_description = models.TextField(verbose_name='Полное содержание статьи',
                                        default='содержание')

    image = models.ImageField(upload_to='articles/',
                              null=True, blank=True, verbose_name='Фото статьи')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата обноваления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    author = models.ForeignKey(to=User, on_delete=models.CASCADE,
                               editable=False, verbose_name='Автор статьи',
                               default=1)

    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_absolute_url(self):
        return reverse('blog_single', kwargs={'slug': self.slug})

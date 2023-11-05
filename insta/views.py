from django.shortcuts import render, redirect
from .models import Car, Profile, Review
from django.contrib.auth import login, logout

from .forms import *


def index(request):
    car_prds = Car.objects.all()
    content = {
        'title': 'Главная страница',
        'car_prds': car_prds,
    }

    return render(request, 'insta/index.html', content)


def about(request):
    content = {
        'title': 'О нас'
    }

    return render(request, 'insta/about.html', content)


def services(request):
    content = {
        'title': 'Наши услуги',
    }

    return render(request, 'insta/services.html', content)


def pricing(request):
    content = {
        'title': 'Цены',
    }

    return render(request, 'insta/pricing.html', content)


def car(request):
    car_prds = Car.objects.all()

    content = {
        'car_prds': car_prds,
        'title': 'Машины',
    }

    return render(request, 'insta/car.html', content)


def blog(request):
    articles = Article.objects.all()
    content = {
        'title': 'Блог',
        'articles': articles,
    }

    return render(request, 'insta/blog.html', content)


def contact(request):
    content = {
        'title': 'Контакты',
    }

    return render(request, 'insta/contact.html', content)


def blog_single(request, slug):
    article = Article.objects.get(slug=slug)
    articles = Article.objects.all()
    context = {
        'title': 'Детальное описание блога',
        'article': article,
    }

    return render(request, 'insta/blog_single.html', context)


def car_single(request, slug):
    car_prd = Car.objects.get(slug=slug)
    car_prds = Car.objects.all()

    import random
    rec = random.choices(car_prds, k=3)

    # reviews = Review.objects.filter(car_prd=car_prd)

    context = {
        'title': car_prd.title,
        'car_prd': car_prd,
        'rec': rec,
        'reviews': 'reviews',
    }
    if request.user.is_authenticated:
        context['review_form'] = ReviewForm()
    return render(request, 'insta/car_single.html', context)


def registration_user(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            # success message
            return redirect('login_user')
        else:
            # error message
            return redirect('registration_user')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
        'title': 'Регистрация пользователя'
    }
    return render(request, 'insta/registration_user.html', context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                # success message
                return redirect('index')
            else:
                # error message
                return redirect('login_user')
        else:
            # error message
            return redirect('login_user')
    else:
        form = LoginForm()

    context = {
        'form': form,
        'title': 'Вход в аккаунт'
    }

    return render(request, 'insta/login_user.html', context)


def logout_user(request):
    logout(request)
    # success message
    return redirect('index')


def save_review(request, product_id):
    car_prd = Car.objects.get(pk=product_id)
    form = ReviewForm(data=request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user
        review.product = car_prd
        review.save()

        # success message
        return redirect('product_page', car_prd.slug)
    else:
        # error message
        return redirect('product_page', car_prd.slug)

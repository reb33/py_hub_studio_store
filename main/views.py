from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    # categories = Categories.objects.all()

    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Тест о том почему этот магазин такой уникальный",
    }
    return render(request, "main/about.html", context)

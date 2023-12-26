from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME"
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': 'Новые решения в вашем доме'
    }

    return render(request, 'main/about.html', context)
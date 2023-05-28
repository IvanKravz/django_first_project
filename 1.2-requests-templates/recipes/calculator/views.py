from django.shortcuts import render, reverse
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def home_view(request):
    return HttpResponse('Введите в адресной строке через / название блюда: omlet, pasta, buter и через /? количество блюд servings=')


def calculator(request, meal):
    servings = int(request.GET.get('servings', 1))
    context = {'recipe':{}}
    for ingredient, amount in DATA[meal].items():
        context['recipe'][ingredient] = round((amount * servings), 2)
    return render(request, 'calculator/index.html', context)

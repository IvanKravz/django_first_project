from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

DATA = []
path = "C:\\Users\\Xiaom\\Desktop\\Python\\ДЗ\\DJANGO\\dj-homeworks\\1.2-requests-templates\\pagination\\data-398-2018-08-30.csv"
with open(path, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        DATA.append(row)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(DATA, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)


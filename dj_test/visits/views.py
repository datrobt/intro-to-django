from django.shortcuts import render
from random import randint


def index(request):
    context = {"num_visits": randint(1, 5)}
    return render(request, 'index.html', context)

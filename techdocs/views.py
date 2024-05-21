from django.shortcuts import render

from . import models


# Create your views here.
def index(request):
    obj = models.Category.objects.all()
    return render(request, 'techdocs/index.html', {'categories': obj})


def create_category(request):
    return render(request, 'techdocs/create_category.html', {})


def update_category(request):
    return render(request, 'techdocs/update_category.html', {})


def delete_category(request):
    return render(request, 'techdocs/delete_category.html', {})

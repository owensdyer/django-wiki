from django.shortcuts import render

from . import models


# Create your views here.
def index(request):
    obj = models.Supercategory.objects.all()

    return render(request, 'techdocs/index.html', {'supercategories': obj})


def view_category(request, category):
    # objt = models.Category.objects.get(slug=category)
    # print(objt.parents.all())

    obj = models.Category.objects.all()

    return render(request, 'techdocs/view_category.html', {'categories': obj})


def view_document(request, category, document):
    obj = models.TechnicalDoc.objects.all()
    print(obj)
    return render(request, 'techdocs/view_document.html', {'doc': obj})


def create_category(request):
    return render(request, 'techdocs/create_category.html', {})


def update_category(request):
    return render(request, 'techdocs/update_category.html', {})


def delete_category(request):
    return render(request, 'techdocs/delete_category.html', {})

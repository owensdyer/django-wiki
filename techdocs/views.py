from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'techdocs/index.html', {})


def create_category(request):
    return render(request, 'techdocs/create_category.html', {})


def update_category(request):
    return render(request, 'techdocs/update_category.html', {})


def delete_category(request):
    return render(request, 'techdocs/delete_category.html', {})

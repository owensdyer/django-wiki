from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # viewing urls
    path('<slug:category>/', views.view_category, name='view_category'),
    # path('<slug:category>/<slug:document>/', views.view_document, name='view_document'),

    # creating urls
    # path('create/category/', views.create_category, name='create_category'),
    # path('create/document/', views.create_document, name='create_document'),
    #
    # # updating urls
    # path('update/<slug:category>', views.update_document, name='update_document'),
    # path('update/<slug:doucment>/', views.update_document, name='update_document'),
    #
    # # deleting urls
    # path('delete/<slug:category>', views.delete_document, name='delete_document'),
    # path('delete/<slug:document>', views.delete_document, name='delete_document'),
]

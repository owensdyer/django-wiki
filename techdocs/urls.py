from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # category urls
    path('category/create/', views.create_category, name='create_category'),
    path('category/update/<int:pk>/', views.update_category, name='edit_category'),
    path('category/delete/<int:pk>/', views.delete_category, name='delete_category'),

    # technical documentation
    path('document/create/', views.create_category, name='create_category'),
    path('document/update/<slug:pk>/', views.update_category, name='edit_category'),
    path('document/delete/<slug:pk>/', views.delete_category, name='delete_category'),
]

from django.urls import path

from .views import home

urlpatterns = [
    #path('URL-name', 'function_name')
    # url-name = blank ให้เป็น homepage
    path("", home)
]
from django.urls import path

from .views import home, post_detail

urlpatterns = [
    #path('URL-name', 'function_name')
    # url-name = blank ให้เป็น homepage
    path("", home),
    path("posts/<int:post_id>", post_detail)
]
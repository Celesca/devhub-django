from django.urls import path

from .views import home, post_detail, cat_api

urlpatterns = [
    #path('URL-name', 'function_name')
    # url-name = blank ให้เป็น homepage
    path("", home, name="home"), # name = 'home' เพื่อให้ อ้างอิง {% url 'home'}
    path("posts/<int:post_id>", post_detail),
    path("cats", cat_api , name='cat_api')
]
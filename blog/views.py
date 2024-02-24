from django.shortcuts import render
from .models import Post

import requests

# Create your views here.
def home(request):
    # Get all posts Model.objects.all()
    all_posts = Post.objects.all()

    return render(request, 'blog/home.html', {'all_posts': all_posts})

def post_detail(request, post_id):

    single_post = Post.objects.get(pk=post_id)
    
    # Get single post
    return render(request, 'blog/post_detail.html' , {'single_post':single_post})

def cat_api(request):

    # Endpoints ที่จะไป Request
    url = "https://api.thecatapi.com/v1/images/search?limit=10&breed_ids=beng&api_key=live_JTURr2hSvnHD4TGeVnUUuTEQgHi7BuuurpEXTXMgxLfXM27cffSItQwUv7QTUBP2"
    API_KEY = "live_JTURr2hSvnHD4TGeVnUUuTEQgHi7BuuurpEXTXMgxLfXM27cffSItQwUv7QTUBP2"

    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }

    res = requests.get(url, headers)
    cats = res.json()
    
    cat_info = []
    for cat in cats:
        cat_breeds = cat.get('breeds', [])
        if cat_breeds:
            breed = cat_breeds[0]
            cat_info.append({
                'name': breed.get('name'),
                'image': cat.get('url'),
                'breed': breed.get('description')
            })

    # pip install requests
    return render(request, 'blog/cat.html', {'cats': cat_info})
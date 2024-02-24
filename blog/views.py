from django.shortcuts import render
from .models import Post

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

    # pip install requests
    return render(request, 'blog/cat.html')
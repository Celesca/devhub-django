from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    # Get all posts Model.objects.all()
    all_posts = Post.objects.all()

    return render(request, 'blog/home.html', {'all_posts': all_posts})

def post_detail(request, post_id):
    
    # Get single post
    return render(request, )
from django.shortcuts import render, HttpResponse
from random import randint
from posts.models import Post

# Create your views here.
def home_view(request):
    return render(request, "base.html")

def test_view(request):
    return HttpResponse(f"Hello Alex {randint(1,10)}")

def html_views(request):
    return render(request, "base.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render (request, "posts/post_list.html", context={"posts": posts})
from django.shortcuts import render, HttpResponse, redirect
from random import randint
from posts.models import Post
from posts.forms import PostForm

# Create your views here.
def home_view(request):
    if request.method == "GET":
       return render(request, "base.html")

def test_view(request):
    if request.method == "GET":
       return HttpResponse(f"Hello Alex {randint(1,10)}")

def html_views(request):
    if request.method == "GET":
       return render(request, "base.html")

def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render (request, "posts/post_list.html", context={"posts": posts})

def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "posts/post_detail.html", context={"post": post})
    
def post_create_view(request):
    if request.method == "GET":
        form = PostForm
        return render(request, "posts/post_create.html", context={"form":form})
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        rate = request.POST.get("rate")
        image = request.FILES.get("image")
        try:
           post = Post.objects.create(title=title, content=content, rate=rate, image=image)
           return redirect("/posts")
        except Exception as x:
            return HttpResponse (f"Error {x}")



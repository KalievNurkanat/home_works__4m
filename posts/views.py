from django.shortcuts import render, HttpResponse, redirect
from random import randint
from posts.models import Post
from posts.forms import PostForm2, SearchForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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


@login_required(login_url="/login/")
def post_list_view(request):
    posts = Post.objects.all()
    form = SearchForm()
    if request.method == "GET":
        query_params = request.GET
        search = query_params.get("search")
        category_id = query_params.get("category_id")
        tags_ids = query_params.getlist("tags_ids")
        if search:
            posts = posts.filter(Q(Q(title__icontains=search) |  Q(content__icontains=search)))
        if category_id:
            posts = posts.filter(category_id=category_id)
        if tags_ids:
            posts = posts.filter(tags__id__in=tags_ids).distinct()

        return render (request, "posts/post_list.html", context={"posts": posts, "form":form})


@login_required(login_url="/login/")
def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "posts/post_detail.html", context={"post": post})


@login_required(login_url="/login/")
def post_create_view(request):
    if request.method == "GET":
        form = PostForm2
        return render(request, "posts/post_create.html", context={"form":form})
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form":form})
        
        try:
           form.save()
           return redirect("/posts")
        except Exception as x:
            return HttpResponse (f"Error {x}")



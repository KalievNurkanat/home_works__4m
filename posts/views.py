from django.shortcuts import render, HttpResponse
from random import randint

# Create your views here.
def test_view(request):
    return HttpResponse(f"Hello Alex {randint(1,10)}")


def html_views(request):
    return render(request, "posts/base.html")

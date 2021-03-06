import django
from django.shortcuts import render
from blog.models import Category, Post
from django.views import generic

# Create your views here.
def index(req):
    post_latest = Post.objects.order_by('-createDate')[:6]  #포스트에서 최신순으로 6개 가져옴
    context = {
        "post_latest": post_latest
    }
    return render(req, 'index.html', context=context)

class PostDetailView(generic.DetailView):
    model = Post

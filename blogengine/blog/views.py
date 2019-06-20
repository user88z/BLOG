from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts':posts})
    

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})

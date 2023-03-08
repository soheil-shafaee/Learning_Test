from django.shortcuts import render
from .models import Post


def post_list_view(request):
    all_posts = Post.objects.all()
    return render(request, 'home/posts_list.html', {"post_list": all_posts})

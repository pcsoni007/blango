from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
# Create your views here.
def index(request):
    post = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", { 'posts':post })

def bootstrap(request):
    return render(request, "blog/exbootstrap.html")

def getPostDetails(request,slug):
    post = get_object_or_404(Post, slug=slug)
    print("Post ID", post.id, post.slug)
    return render(request, "blog/post-detail.html", { "post":post })
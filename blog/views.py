from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.utils import timezone
from blog.forms import CommentForm
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

def index(request):
    post = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", { 'posts':post })

def bootstrap(request):
    return render(request, "blog/exbootstrap.html")

def getPostDetails(request,slug):
    post = get_object_or_404(Post, slug=slug)
    # comment_form = None
    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    return render(
        request, "blog/post-detail.html", {"post": post, "comment_form": comment_form}
    )
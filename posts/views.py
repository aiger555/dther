from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
 
from .models import Post
from .forms import PostForm
from .utils import  ObjectUpdateMixin, ObjectDeleteMixin



User = get_user_model()

def posts_list_view(request):
    
    if request.method == 'GET':
        if request.user.is_authenticated:
            posts = request.user.posts.all()
        else:
            posts = Post.objects.all()

        return render(request, 'posts/index.html', context = {'posts': posts})


def post_detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_detail.html',
                          {'post': post})


class PostCreateView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('login_url'))
        form = PostForm()
        return render(request, 'posts/post_create.html', context={'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post)
        return render(request, 'posts/post_create.html', context={'form': form})


class PostUpdateView(View, ObjectUpdateMixin):
    bound_form = PostForm
    template = 'posts/post_update.html'
    obj_class = Post


class PostDeleteView(View, ObjectDeleteMixin):
    template = 'posts/post_delete.html'
    obj_class = Post
    redirect_template = 'posts_list_url'

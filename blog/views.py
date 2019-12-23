from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.db import transaction
# Create your views here.

# class Login(TemplateView):
#     template_name = 'blog/login.html'

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        # - recent up

class PostDetailView(DetailView):
    ATOMIC_REQUESTS = True
    model = Post

class PostDetailView1(DetailView):
    ATOMIC_REQUESTS = True
    model = Post
    template_name = 'blog/post_detail_like.html'

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    # context_object_name = 'drafts_list'
    login_url = '/login/'


    redirect_field_name = 'blog/post_draft_list.html'
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
        return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def add_like_to_post(request,pk):
    ATOMIC_REQUESTS = True
    post = get_object_or_404(Post,pk=pk)
    post.increase_like()
    return redirect('post_detail_like',pk=post.pk)

@login_required
def remove_like_to_post(request,pk):
    ATOMIC_REQUESTS = True
    post = get_object_or_404(Post,pk=pk)
    post.decrease_like()
    return redirect('post_detail',pk=post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

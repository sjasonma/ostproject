from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from myblog.models import Blog, Post, Tag

class IndexView(generic.ListView):
	model = Blog
	template_name = 'index.html'

class BlogView(generic.DetailView):
	model = Blog
	template_name = 'blog.html'

class PostView(generic.DetailView):
	model = Post
	template_name = 'post.html'

def sign_up_view(request):
	data_dict = {}
	return render(request, 'sign_up.html', data_dict)

def sign_in_view(request):
	data_dict = {}
	return render(request, 'sign_in.html', data_dict)

@login_required
def my_blogs_view(request):
	data_dict = {}
	return render(request, 'my_blogs.html', data_dict)

@login_required
def create_post_view(request, blog_id=None):
	data_dict = {}
	data_dict['blog_id'] = blog_id
	return render(request, 'create_post.html', data_dict)

@login_required
def edit_post_view(request, post_id=None):
	data_dict = {}
	post = get_object_or_404(Post, pk=post_id)
	data_dict['post'] = post
	data_dict['blog_id'] = post.blog.id
	tag_list = []
	for tag in post.tags.all():
		tag_list.append(tag.name)
	tags = ", ".join(tag_list)
	data_dict['tags'] = tags
	return render(request, 'edit_post.html', data_dict)

@login_required
def create_blog_view(request):
	data_dict = {}
	return render(request, 'create_blog.html', data_dict)

@login_required
def share_blog_view(request, blog_id=None):
	data_dict = {}
	data_dict['blog_id'] = blog_id
	blog = get_object_or_404(Blog, pk=blog_id)
	author_list = []
	for author in blog.authors.all():
		author_list.append(author.username)
	authors = ", ".join(author_list)
	data_dict['authors'] = authors
	return render(request, 'share_blog.html', data_dict)




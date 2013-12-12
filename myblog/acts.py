from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from myblog import constant
from myblog.models import Blog, Post, Tag

def sign_in(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return redirect(reverse('myblog:index'))
	else:
		return HttpResponse("Account Password Incorrect!")

def sign_up(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	first_name = request.POST.get('first_name')
	last_name = request.POST.get('last_name')
	email = request.POST.get('email')
	if not username:
		return HttpResponse('Username cannot be blank!')
	exist = User.objects.filter(username = username)
	if len(exist) < 1:
		user = User()
		user.set_password(password)
		user.username = username
		user.first_name = first_name
		user.last_name = last_name
		user.email = email
		user.save()
		user = authenticate(username=username, password=password)
		login(request,user)
		return HttpResponseRedirect(reverse('myblog:index'))
	else:
		return HttpResponse("This one has been used. Please choose another one.")



@login_required
def sign_out(request):
	logout(request)
	return redirect(reverse('myblog:index'))

@login_required
def create_post(request):
	user = request.user
	blog_id = request.POST.get('blog_id')
	blog = Blog.objects.get(pk = blog_id)
	post_id = request.POST.get('post_id')
	if user not in blog.authors.all():
		return HttpResponse("Sorry you are not authorized to post here")
	else:
		if post_id:
			post = Post.objects.get(pk=post_id)
			if user != post.author:
				return HttpResponse("Sorry you are not authorized to edit here")
		else:
			post = Post()
		post.author = user
		post.blog = blog
		post.title = request.POST.get('title')
		post.body = request.POST.get('body')
		
		tags = request.POST.get('tags')
		tag_names = tags.split(',')
		if not tags.strip():
			tag_names = [constant.NO_TAG]
		tag_set = set(tag_names)
		tag_list = []
		for tname in tag_set:
			tname_s = tname.strip()
			try:
				tag = Tag.objects.get(name__iexact=tname_s)
			except Tag.DoesNotExist:
				tag = None
			if not tag:
				tag = Tag()
				tag.name = tname_s
				tag.save()
			tag_list.append(tag)
		post.save()
		post.tags = tag_list;
		post.save()
		return HttpResponseRedirect(reverse('myblog:index'))

@login_required
def edit_post(request):
	return create_post(request)

@login_required
def delete_post(request, post_id=None):
	user = request.user
	post = Post.objects.get(pk=post_id)
	if user == post.author:
		post.delete()
	else:
		return HttpResponse("Sorry you are not authorized to delete this post.")
	return HttpResponseRedirect(reverse('myblog:index'))

@login_required
def create_blog(request):
	user = request.user
	blog = Blog()
	blog.name = request.POST.get('name')
	blog.owner = user
	authors = []
	authors.append(user)
	blog.save()
	blog.authors = authors
	blog.save()
	return HttpResponseRedirect(reverse('myblog:index'))

@login_required
def share_blog(request):
	blog_id = request.POST.get('blog_id')
	blog = get_object_or_404(Blog, pk=blog_id)
	usernames = request.POST.get('usernames')
	username_list = usernames.replace(" ", "").split(',')
	username_list.append(request.user.username)
	username_set = set(username_list)
	author_list = []
	for uname in username_set:
		try:
			user = User.objects.get(username=uname)
		except User.DoesNotExist:
			user = None
		if user:
			author_list.append(user)
	blog.authors = author_list
	blog.save()
	return HttpResponseRedirect(reverse('myblog:index'))

@login_required
def delete_blog(request, blog_id=None):
	user = request.user
	blog = Blog.objects.get(pk=blog_id)
	if user == blog.owner:
		for post in blog.post_set.all():
			post.delete()
		blog.delete()
	else:
		return HttpResponse("Sorry you are not authorized to delete this blog.")
	return HttpResponseRedirect(reverse('myblog:index'))





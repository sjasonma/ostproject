from django.conf.urls import patterns, url

from myblog import views, acts

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^blog/(?P<pk>\d+)$', views.BlogView.as_view(), name='blog'),
    url(r'^post/(?P<pk>\d+)$', views.PostView.as_view(), name='post'),
    url(r'^sign_up$', views.sign_up_view, name='sign_up'),
    url(r'^sign_up_act$', acts.sign_up, name='sign_up_act'),
    url(r'^sign_in$', views.sign_in_view, name='sign_in'),
    url(r'^sign_in_act$', acts.sign_in, name='sign_in_act'),
    url(r'^sign_out$', acts.sign_out, name='sign_out'),
    url(r'^my_blogs$', views.my_blogs_view, name='my_blogs'),
    url(r'^blog/(?P<blog_id>\d+)/create_post$', views.create_post_view, name='create_post'),
    url(r'^create_post_act$', acts.create_post, name='create_post_act'),
    url(r'^blog/(?P<post_id>\d+)/edit_post$', views.edit_post_view, name='edit_post'),
    url(r'^edit_post_act$', acts.edit_post, name='edit_post_act'),
    url(r'^blog/(?P<post_id>\d+)/delete_post$', acts.delete_post, name='delete_post'),
    url(r'^create_blog$', views.create_blog_view, name='create_blog'),
    url(r'^create_blog_act$', acts.create_blog, name='create_blog_act'),
    url(r'^blog/(?P<blog_id>\d+)/share_blog$', views.share_blog_view, name='share_blog'),
    url(r'^share_blog_act$', acts.share_blog, name='share_blog_act'),
    url(r'^blog/(?P<blog_id>\d+)/delete_blog$', acts.delete_blog, name='delete_blog'),
)
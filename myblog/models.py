from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name="owner_blogs")
    authors = models.ManyToManyField(User, related_name="author_blogs")
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=400)
    body = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.title

    def get_body(self):
        return self.body.replace('\n','<br>')
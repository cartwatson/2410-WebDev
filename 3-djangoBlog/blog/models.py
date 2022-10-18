from statistics import mode
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# TODO: MAKE MODELS
# BLOG
class blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    posted = models.DateTimeField()
    def __str__(self):
        return self.content
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_content(self):
        return self.content
    def get_posted(self):
        return self.posted

# COMMENT
class comment(models.Model):
    blog = models.ForeignKey('blog', on_delete=models.CASCADE) # NEEDS TO AND ON_DELETE
    commenter = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    posted = models.DateTimeField()
    def __str__(self):
        return self.content
    def get_blog(self):
        return self.blog
    def get_commenter(self):
        return self.commenter
    def get_email(self):
        return self.email
    def get_content(self):
        return self.content
    def get_posted(self):
        return self.posted
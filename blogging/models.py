from django.db import models
from django.contrib.auth.models import User

# blogging/models.py


class Poll(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Post(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

class Category(models.Model):

    def __str__(self):
        return self.name

#    name = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True,)



    #post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)



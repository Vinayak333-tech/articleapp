from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    thumb = models.ImageField(default='default.png',blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # add in thumbnail and author later
    def snippet(self):
        return self.body[:50] + "..."

from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=50000)
    link = models.TextField(default="")
    detail = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True)


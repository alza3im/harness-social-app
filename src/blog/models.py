from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="blogpost", blank=True
    )

    def __str__(self):
        return self.title

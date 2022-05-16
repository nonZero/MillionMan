from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=300)
    posted_at = models.DateTimeField(default=timezone.now)
    teaser = models.TextField()
    content = models.TextField()

    class Meta:
        ordering = ["-posted_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.id})

from __future__ import unicode_literals

from django.utils import timezone
from django.db import models


class Post(models.Model):
    """Create blog post model and save it in db"""
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Save and publish post with current time as publish time"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """Return string with post title"""
        return self.title

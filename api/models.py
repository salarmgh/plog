from django.db import models
from authz.models import User
from django.utils.translation import ugettext_lazy as _

class Posts(models.Model):
    title = models.CharField(_('post title'), max_length=128, blank=False, )
    content = models.TextField(_('post content'), blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    content = models.CharField(_('comment content'), max_length=512, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

class PostLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('user', 'post',)

class CommentLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('user', 'comment',)

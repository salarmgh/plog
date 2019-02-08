from rest_framework import serializers
from api.models import Posts, User, Comments, PostLikes, CommentLikes
from authz.serializers import UserBaseSerializer
from pprint import pprint

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'user', 'title', 'content', 'created_at')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'user', 'post', 'content', 'created_at')

class PostLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikes
        fields = ('user', 'post', 'created_at')

class CommentLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLikes
        fields = ('id', 'user', 'comment', 'created_at')

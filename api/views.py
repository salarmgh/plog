from django.shortcuts import render
from rest_framework import viewsets
from api.models import Posts, Comments, PostLikes, CommentLikes
from api.serializers import PostsSerializer, CommentsSerializer, PostLikesSerializer, CommentLikesSerializer
import django_filters.rest_framework

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('user',)

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('user','post')

class PostLikesViewSet(viewsets.ModelViewSet):
    queryset = PostLikes.objects.all()
    serializer_class = PostLikesSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('user','post')

class CommentLikesViewSet(viewsets.ModelViewSet):
    queryset = CommentLikes.objects.all()
    serializer_class = CommentLikesSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('user','comment')

"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.conf.urls import url, include
from authz.views import UserViewSet
from api.views import PostsViewSet, CommentsViewSet, PostLikesViewSet, CommentLikesViewSet
from rest_framework import routers
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostsViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'postlikes', PostLikesViewSet)
router.register(r'commentlikes', CommentLikesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
   from django.contrib.staticfiles import views

   urlpatterns += [
       url(r'^static/(?P<path>.*)$', views.serve),
   ]

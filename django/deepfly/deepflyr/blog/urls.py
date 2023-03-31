from . import views
from django.urls import path
from .feeds import  LatestPostsFeed , AtomSiteNewsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    #path('', views.PostList.as_view(), name='home'),
    path('', views.PostList, name='home'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
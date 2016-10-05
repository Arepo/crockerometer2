from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^([0-9]+)$',     views.detail,      name='detail'),
  url(r'^$',             views.index),
  url(r'^post_metric/$', views.post_metric, name='post_metric'),
  url(r'^post_vote/$',   views.post_vote,   name='post_vote')
]

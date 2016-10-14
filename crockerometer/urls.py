from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^user/(\w+)/$',  views.profile,     name='profile'),
  url(r'^([0-9]+)$',     views.detail,      name='detail'),
  url(r'^$',             views.index),
  url(r'^post_metric/$', views.post_metric, name='post_metric'),
  url(r'^post_vote/$',   views.post_vote,   name='post_vote'),
  url(r'^login/$',       views.login_view,  name='login'),
  url(r'^logout/$',      views.logout_view, name='logout'),
  url(r'^register/$',    views.register,    name='register')
]

from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^([0-9]+)$',  views.detail,      name='detail'),
  url(r'^$',          views.index),
  url(r'^post_url/$', views.post_woojit, name='post_woojit')
]

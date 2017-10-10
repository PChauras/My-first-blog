from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.post_list, name='post_list'),
url(r'^post/new/^', 'blog.views.post_new', name='post_new'),
url(r'^post/new/$', 'blog.views.post_new', name='post_new'),
url(r'^calc$', 'blog.views.post_calc', name='post_calc'),
]
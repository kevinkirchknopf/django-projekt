from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path



urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls import patterns, include, url
from api import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'^reload$', views.reload_api, name="reload"),
                       url(r'^fetch/(\d+)/$', views.fetch, name="fetch"),
                       url(r'^put/$', views.put, name="put"),
                       )

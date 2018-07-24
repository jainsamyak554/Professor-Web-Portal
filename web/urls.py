from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'web'

urlpatterns = [

    url(r'^([0-9]+)/(?P<pk>[0-9]+)/publications/$', views.publicationview.as_view(), name='publicationview'),
    url(r'^([0-9]+)/(?P<pk>[0-9]+)/about/$', views.aboutview.as_view(), name='aboutview'),
    url(r'^([0-9]+)/(?P<prof_id>[0-9]+)/about/1$', views.updatepost, name='postupdate'),
    url(r'^([0-9]+)/(?P<pk>[0-9]+)/about/update$', views.infoupdate.as_view(), name='infoupdate'),
    url(r'^([0-9]+)/(?P<pk>[0-9]+)/students/$', views.studentview.as_view(), name='studentview'),
    url(r'^([0-9]+)/(?P<pk>[0-9]+)/recognition/$', views.recognitionview.as_view(), name='recognitionview'),
    url(r'^([0-9]+)/(?P<pk>[0-9]+)/project/$', views.projectview.as_view(), name='projectview'),
    url(r'^([0-9]+)/(?P<pk>[0-9]+)/teaching/$', views.teachingview.as_view(), name='teachingview'),
    url(r'^register/$', views.userformview.as_view(), name='register'),
    url(r'^([0-9]+)/(?P<prof_id>[0-9]+)/teaching/create$',views.teachingcreate, name='teachingcreate'),
    url(r'^(?P<pk>[0-9]+)/teachingupdate$',views.teachingupdate.as_view(), name='teachingupdate'),
    url(r'^(?P<pk>[0-9]+)/publicationupdate$',views.publicationupdate.as_view(), name='publicationupdate'),
    url(r'^(?P<pk>[0-9]+)/projectupdate$',views.projectupdate.as_view(), name='projectupdate'),
    url(r'^(?P<pk>[0-9]+)/recognitionupdate$',views.recognitionupdate.as_view(), name='recognitionupdate'),
    url(r'^([0-9]+)/(?P<prof_id>[0-9]+)/publications/create$',views.publicationcreate, name='publicationcreate'),
    url(r'^([0-9]+)/(?P<prof_id>[0-9]+)/recognition/create$',views.recognitioncreate, name='recognitioncreate'),
    url(r'^([0-9]+)/(?P<prof_id>[0-9]+)/project/create$',views.projectcreate, name='projectcreate'),
    url(r'^$', views.homeview, name='homeview'),
    url(r'^(?P<dept_id>[0-9]+)/$', views.deptview, name='deptview'),
    url(r'^create/$',views.infocreate.as_view(), name='infocreate'),


]


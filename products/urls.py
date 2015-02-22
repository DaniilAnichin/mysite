from django.conf.urls import patterns, url
from products.views import *


urlpatterns = patterns('',
    url(r'^$',  IndexView.as_view(), name='index'),
    url(r'^page(?P<page>\d+)/$',  IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$',  DetailView.as_view(), name='detail'),
    url(r'^select/$', selection, name='search'),
    url(r'^select/page(?P<page>\d+)/$', selection, name='search'),
    url(r'^creation/$',  CreateProductionView.as_view(), name='creation'),
)

from django.conf.urls import patterns, url
from products import views


urlpatterns = patterns('',
    url(r'^$', views.selection, name='selection'),
    url(r'^select/$', views.selection, name='selection'),
    url(r'^(?P<pk>\d+)/$',  views.DetailView.as_view(), name='detail'),
    url(r'^creation/$',  views.CreateProductionView.as_view(), name='creation'),
    url(r'^search/$',  views.search_look, name='search'),
)
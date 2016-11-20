from django.conf.urls import url
from products.views import *


urlpatterns = [
    url(r'^$', selection, name='search'),
    url(r'^select/$', selection, name='search'),
    url(r'^(?P<pk>\d+)/$',  DetailView.as_view(), name='detail'),
    url(r'^creation/$',  CreateProductionView.as_view(), name='creation'),
]

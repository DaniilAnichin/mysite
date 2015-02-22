from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^friends_mapping/', include('friends_mapping.urls', namespace="friends")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include('products.urls', namespace="products")),
)

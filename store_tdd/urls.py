from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'store.views.home', name='home'),
    url(r'^cart/(?P<cart_id>\d+)/$', 'store.views.cart', name='view_cart'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

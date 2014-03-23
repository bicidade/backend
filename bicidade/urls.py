from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from bicidade import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bemok.views.home', name='home'),
    # url(r'^bemok/', include('bemok.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^reverse_geocode/$', views.reverse_geocode, name='reverse_geocode'),
    url(r'^route/$', views.route, name='route'),
)

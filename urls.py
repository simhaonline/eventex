from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', { 'template': 'index.html' }),
    url(r'^subscription/', include('subscription.urls', namespace='subscription')),
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^eventex/', include('eventex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

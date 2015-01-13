from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PuffMaster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^controlpanel/', include('control_panel.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

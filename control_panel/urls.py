from django.conf.urls import patterns, url

from control_panel import views

urlpatterns = patterns('',
	url(r'^$', views.dashboard, name='dashboard')
)
from django.conf.urls import include, url
from toasauti import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new-report/$', views.new_report, name='new_report'),
    url(r'^create-report/$', views.create_report, name='create_report'),
    url(r'^about/$', views.about, name='about'),
    url(r'^ussd/$', views.ussd, name='ussd'),
    url(r'^create-feedback/$', views.create_feedback, name='create_feedback'),
]

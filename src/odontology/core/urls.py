from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.principal, name='principal'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^version/$', views.version, name='version'),
    url(r'^mp/$', views.mp, name='mp'),
]

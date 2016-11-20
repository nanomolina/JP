from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.principal, name='principal'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^version/$', views.version, name='version'),
    url(r'^mp/$', views.mp, name='mp'),
    url(r'^tariff/$', views.tariff, name='tariff'),
    url(r'^birthdays/$', views.birthdays, name='birthdays'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
]

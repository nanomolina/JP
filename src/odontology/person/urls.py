from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^patient/$', views.patients, name='patient_list'),
    url(r'^patient/(?P<id>[0-9]+)/$', views.patient_profile, name='patient_profile'),
    url(r'^clinical_history/(?P<id>[0-9]+)/$', views.clinical_history, name='clinical_history'),
    url(r'^patient/edit/(?P<id>[0-9]+)/$', views.edit_patient, name='edit_patient'),
    url(r'^patient/remove/(?P<id>[0-9]+)/$', views.remove_patient, name='remove_patient'),
    url(r'^patient/search/$', views.search_patient, name='search_patient'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/personal/$', views.settings_personal, name='settings_personal'),
    url(r'^settings/dentist/$', views.settings_dentist, name='settings_dentist'),
    url(r'^reset_password/$', views.reset_password, name='reset_password'),
]

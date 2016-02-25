from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^patient/$', views.list_patients, name='patient_list'),
    url(r'^patient/(?P<id>[0-9]+)/$', views.patient_profile, name='patient_profile'),
    url(r'^patient/edit/(?P<id>[0-9]+)/$', views.edit_patient, name='edit_patient'),
]

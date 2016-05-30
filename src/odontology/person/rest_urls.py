from django.conf.urls import url

from . import rest_views

urlpatterns = [
    url(r'^patient-list/$', rest_views.patient_list, name='patient_list'),
]

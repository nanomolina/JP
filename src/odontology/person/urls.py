from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^patient/$', views.list_patients, name='patient_list'),
]

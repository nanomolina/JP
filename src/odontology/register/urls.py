from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new_benefit/(?P<patient_id>[0-9]+)/$', views.new_benefit, name='new_benefit'),
    url(r'^benefit_detail/edit/(?P<detail_id>[0-9]+)/$', views.edit_benefit_detail, name='edit_benefit_detail'),
]

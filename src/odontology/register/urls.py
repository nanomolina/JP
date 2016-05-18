from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^benefit/new/(?P<patient_id>[0-9]+)/$', views.new_benefit, name='new_benefit'),
    url(r'^benefit/edit/(?P<patient_id>[0-9]+)/$', views.edit_benefit, name='edit_benefit'),
    url(r'^benefit_detail/(?P<patient_id>[0-9]+)/edit/(?P<detail_id>[0-9]+)/$', views.edit_benefit_detail, name='edit_benefit_detail'),
    url(r'^benefit/(?P<patient_id>[0-9]+)/to_pdf/(?P<bf_id>[0-9]+)/$', views.benefit_to_pdf, name='benefit_to_pdf'),
    url(r'^odontogram/edit/(?P<patient_id>[0-9]+)/$', views.edit_odontogram, name='edit_odontogram'),
    url(r'^acumulate_benefit/(?P<patient_id>[0-9]+)/$', views.acumulate_benefit, name='acumulate_benefit'),
    url(r'^radiography/(?P<patient_id>[0-9]+)/edit/(?P<bf_id>[0-9]+)/$', views.edit_radiography, name='edit_radiography'),
    url(r'^record/new/(?P<patient_id>[0-9]+)/$', views.new_record, name='new_record'),
    url(r'^record/edit/(?P<record_id>[0-9]+)/$', views.edit_record, name='edit_record'),
    url(r'^record/remove/(?P<record_id>[0-9]+)/$', views.remove_record, name='remove_record'),
    url(r'^record/account/edit/(?P<record_id>[0-9]+)/$', views.edit_record_account, name='edit_record_account'),
]

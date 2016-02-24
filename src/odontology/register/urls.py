from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^benefit/new/(?P<patient_id>[0-9]+)/$', views.new_benefit, name='new_benefit'),
    url(r'^benefit/edit/(?P<patient_id>[0-9]+)/$', views.edit_benefit, name='edit_benefit'),
    url(r'^benefit_detail/(?P<patient_id>[0-9]+)/edit/(?P<detail_id>[0-9]+)/$', views.edit_benefit_detail, name='edit_benefit_detail'),
    url(r'^pdf/$', views.pdf_example, name='to_pdf'),

]

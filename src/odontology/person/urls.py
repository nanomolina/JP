from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^patient/$', views.patients, name='patient_list'),
    url(r'^social_work/(?P<id>[0-9]+)/$', views.social_work, name='social_work'),
    url(r'^clinical_history/(?P<id>[0-9]+)/$', views.clinical_history, name='clinical_history'),
    url(r'^odontogram/(?P<id>[0-9]+)/$', views.odontogram, name='odontogram'),
    url(r'^patient/profile/(?P<id>[0-9]+)/$', views.profile_patient, name='profile_patient'),
    url(r'^patient/account/(?P<id>[0-9]+)/$', views.accounts, name='accounts'),
    url(r'^patient/edit/(?P<id>[0-9]+)/$', views.edit_patient, name='edit_patient'),
    url(r'^patient/upload_picture/(?P<id>[0-9]+)/$', views.upload_picture, name='upload_picture'),
    url(r'^patient/remove/(?P<id>[0-9]+)/$', views.remove_patient, name='remove_patient'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/personal/$', views.settings_personal, name='settings_personal'),
    url(r'^settings/dentist/$', views.settings_dentist, name='settings_dentist'),
    url(r'^reset_password/$', views.reset_password, name='reset_password'),
    url(r'^registers/$', views.registers, name='registers'),
    url(r'^registers/accounts/$', views.accounts_registers, name='accounts_registers'),
    url(r'^registers/accounts/data/$', views.accounts_registers_data, name='accounts_registers_data'),
]

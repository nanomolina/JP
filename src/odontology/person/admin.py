from django.contrib import admin
from person.models import Dentist, Patient, SocialWork

class DentistAdmin(admin.ModelAdmin):
    fields = ('user', 'circle', 'register_number', 'carrying_home')
admin.site.register(Dentist, DentistAdmin)


class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)


class SocialWorkAdmin(admin.ModelAdmin):
    fields = ('name', 'initial')
admin.site.register(SocialWork, SocialWorkAdmin)

from django.contrib import admin
from person.models import Dentist, Patient, SocialWork, Odontogram, Tooth

class DentistAdmin(admin.ModelAdmin):
    fields = ('user', 'circle', 'register_number', 'carrying_home')
admin.site.register(Dentist, DentistAdmin)


class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)


class SocialWorkAdmin(admin.ModelAdmin):
    fields = ('name', 'initial')
admin.site.register(SocialWork, SocialWorkAdmin)


class ToothInline(admin.TabularInline):
    model = Tooth
    raw_id_fields = ('odontogram', )


class OdontogramAdmin(admin.ModelAdmin):
    fields = ('teeth_number', 'observations', 'month', 'year')
    inlines = [
        ToothInline,
    ]
admin.site.register(Odontogram, OdontogramAdmin)

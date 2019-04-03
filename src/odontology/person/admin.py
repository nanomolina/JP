from django.contrib import admin

from person.models import Dentist, Odontogram, Patient, SocialWork, Tooth


class DentistAdmin(admin.ModelAdmin):
    fields = ('user', 'circle', 'register_number', 'carrying_home')
admin.site.register(Dentist, DentistAdmin)


def create_code(modeladmin, request, queryset):
    amount = 1
    for patient in queryset.order_by('id'):
        patient.code = 'P%04d' % (amount)
        patient.save()
        amount += 1
create_code.short_description = "Crear codigo"


class PatientAdmin(admin.ModelAdmin):
    list_filter = ('dentist', 'active')
    actions = [create_code]
admin.site.register(Patient, PatientAdmin)


class SocialWorkAdmin(admin.ModelAdmin):
    fields = ('name', 'initial')
admin.site.register(SocialWork, SocialWorkAdmin)


class ToothInline(admin.TabularInline):
    model = Tooth
    raw_id_fields = ('odontogram', )
    extra = 0


class OdontogramAdmin(admin.ModelAdmin):
    fields = ('teeth_number', 'observations', 'month', 'year')
    inlines = [
        ToothInline,
    ]
admin.site.register(Odontogram, OdontogramAdmin)

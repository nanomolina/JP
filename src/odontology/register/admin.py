from django.contrib import admin
from register.models import Apross, DetailApross, Faces, Benefit, DetailBenefit, Radiography, Record


def apross_create_radiography(modeladmin, request, queryset):
    for bf in queryset:
        Radiography(apross=bf).save()
apross_create_radiography.short_description = "Crear radiografia"

def benefit_create_radiography(modeladmin, request, queryset):
    for bf in queryset:
        Radiography(benefit=bf).save()
benefit_create_radiography.short_description = "Crear radiografia"


class AprossAdmin(admin.ModelAdmin):
    fields = (
        'patient', 'month', 'year', 'managment_code1',
        'managment_code2', 'managment_code3', 'rx_amount',
    )
    actions = [apross_create_radiography]
admin.site.register(Apross, AprossAdmin)


class DetailAprossAdmin(admin.ModelAdmin):
    fields = (
        'day', 'benefit', 'work_done', 'practic_code',
        'element', 'faces'
    )
admin.site.register(DetailApross, DetailAprossAdmin)


class BenefitAdmin(admin.ModelAdmin):
    fields = (
        'patient', 'month', 'year', 'primary_entity',
        'principal_code', 'managment_code', 'rx_amount',
    )
    actions = [benefit_create_radiography]
admin.site.register(Benefit, BenefitAdmin)


class DetailBenefitAdmin(admin.ModelAdmin):
    fields = (
        'day', 'benefit', 'tooth', 'code', 'faces'
    )
admin.site.register(DetailBenefit, DetailBenefitAdmin)


class FacesAdmin(admin.ModelAdmin):
    fields = (
        'name', 'initial'
    )
admin.site.register(Faces, FacesAdmin)


class RadiographyAdmin(admin.ModelAdmin):
    fields = (
        'apross', 'benefit', 'part_number_1', 'finality_1',
        'part_number_2', 'finality_2', 'part_number_3',
        'finality_3'
    )
admin.site.register(Radiography, RadiographyAdmin)


class RecordAdmin(admin.ModelAdmin):
    fields = (
        'patient', 'date', 'treatment', 'faces', 'tooth', 'period_so',
        'state', 'observations', 'state2',
    )
admin.site.register(Record, RecordAdmin)

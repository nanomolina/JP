from django.contrib import admin
from register.models import Apross, DetailApross, Faces, Benefit, DetailBenefit, Radiography


class AprossAdmin(admin.ModelAdmin):
    fields = (
        'patient', 'month', 'year', 'managment_code1',
        'managment_code2', 'managment_code3', 'rx_amount',
    )
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

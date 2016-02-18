from django.contrib import admin
from register.models import Apross, DetailApross


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

from django.contrib import admin
from core.models import Bill, Day, Chapter, Tariff

class DayAdmin(admin.ModelAdmin):
    pass
admin.site.register(Day, DayAdmin)

class BillAdmin(admin.ModelAdmin):
    fields = ('user', 'paid', 'linode_file', 'text')
admin.site.register(Bill, BillAdmin)

class TariffInline(admin.TabularInline):
    model = Tariff
    extra = 1

class ChapterAdmin(admin.ModelAdmin):
    inlines = [
        TariffInline,
    ]
admin.site.register(Chapter, ChapterAdmin)

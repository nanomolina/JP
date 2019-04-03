from django.contrib import admin

from core.models import AnualFees, Bill, Chapter, Day, Message, Tariff


class DayAdmin(admin.ModelAdmin):
    pass
admin.site.register(Day, DayAdmin)

class BillAdmin(admin.ModelAdmin):
    fields = ('user', 'paid', 'linode_file', 'text')
admin.site.register(Bill, BillAdmin)

class AnualFeesAdmin(admin.ModelAdmin):
    pass
admin.site.register(AnualFees, AnualFeesAdmin)

class TariffInline(admin.TabularInline):
    model = Tariff
    extra = 1

class ChapterAdmin(admin.ModelAdmin):
    inlines = [
        TariffInline,
    ]
admin.site.register(Chapter, ChapterAdmin)

class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Message, MessageAdmin)

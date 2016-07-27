from django.contrib import admin
from core.models import Bill, Day

class DayAdmin(admin.ModelAdmin):
    pass
admin.site.register(Day, DayAdmin)

class BillAdmin(admin.ModelAdmin):
    fields = ('user', 'paid', 'url_file', 'text')
admin.site.register(Bill, BillAdmin)

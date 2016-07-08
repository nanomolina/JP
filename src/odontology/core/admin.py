from django.contrib import admin
from core.models import Bill

class BillAdmin(admin.ModelAdmin):
    fields = ('user', 'paid', 'url_file', 'text')
admin.site.register(Bill, BillAdmin)

from django.contrib import admin
from .models import Boarder, Bills


# Register your models here.
class BoarderAdmin(admin.ModelAdmin):
    list_display = ('room_number','first_name', 'last_name','contact_number')

class BillsAdmin(admin.ModelAdmin):
    list_display = ('month','due_date' ,'rent','electricity','water','status')

admin.site.register(Boarder, BoarderAdmin)
admin.site.register(Bills, BillsAdmin)




from django.contrib import admin


from .models import Pupil
@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email_address', 'passport_id', 'payment', 'one_id']
    list_per_page = 8
    list_filter = ['name', 'phone_number', 'email_address', 'passport_id', 'payment', 'one_id']
    search_fields = ['name', 'phone_number', 'email_address', 'passport_id', 'payment', 'one_id']
from django.contrib import admin
from .models import Customer, Status, Region, ActivityType, Activity


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('company', 'status', 'contact_person', 'address', 'region')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'activity_description', 'sold_units', 'price_per_unit', 'date', 'date_next_activity')
    list_filter = ('date', 'activity_type')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Status)
admin.site.register(Region)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityType)
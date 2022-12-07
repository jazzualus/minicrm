from django.contrib import admin
from .models import Customer, Status, Region, ActivityType, Activity#, Profile
from admincharts.admin import AdminChartMixin
from admincharts.utils import months_between_dates
import datetime
import time

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('company', 'status', 'contact_person', 'address', 'region', 'salesman')
    list_filter = ('region', 'salesman', 'status')


@admin.register(Activity)
class ActivityAdmin(AdminChartMixin, admin.ModelAdmin):
    list_display = ('activity_type', 'activity_description', 'sold_units', 'price_per_unit', 'date', 'date_next_activity', 'salesman')
    list_filter = ('date', 'activity_type', 'salesman')

"""
    KODO PLĖTA ATEIČIAI GRAFINEI DALIAI ADMIN SAITE (dėl to neištrinta)

    def get_list_chart_data(self, queryset):
        if not queryset:
            return {}

        # Cannot reorder the queryset at this point
        earliest = min([x.ctime for x in queryset])

        labels = []
        totals = []
        for b in months_between_dates(earliest, datetime.timezone.now()):
            labels.append(b.strftime("%b %Y"))
            totals.append(
                len(
                    [
                        x
                        for x in queryset
                           if x.ctime.year == b.year and x.ctime.month == b.month

                    ]
                )
            )

        return {
            "labels": labels,
            "datasets": [
                {"label": "New accounts", "data": totals, "backgroundColor": "#79aec8"},
            ],
        }
"""

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Status)
admin.site.register(Region)
#admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityType)
#admin.site.register(Profile)
from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from .models import Bank,Telecom,Personal,Cement
# Register your models here.
admin.site.site_title="team ICecream";
admin.site.site_header="Team IceCream Production";


class Register(admin.ModelAdmin):
    list_display=['name','get_amount','give_amount','date_time']
    search_fields=['name','get_amount','give_amount','date_time']
    list_filter=(('date_time',DateRangeFilter),
    )



admin.site.register(Bank,Register)
admin.site.register(Telecom,Register)
admin.site.register(Cement,Register)
admin.site.register(Personal,Register)

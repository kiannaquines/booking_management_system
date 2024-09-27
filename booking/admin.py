from django.contrib import admin
from booking.models import *


admin.site.site_header = 'Sta. Catalina Multi-Purpose Cooperative'
admin.site.site_title = 'Sta. Catalina Multi-Purpose Cooperative'

admin.site.register(Report)
admin.site.register(Truck)
admin.site.register(Booking)
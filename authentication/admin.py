from django.contrib import admin
from authentication.models import *
from django.utils.translation import gettext_lazy as _

class UserAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'username', 'email', 'date_joined', 'last_login')
    fieldsets = (
        (None, {"fields": ("username", "password",)}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email","user_address","user_mobile_number")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_type",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(User, UserAdmin)
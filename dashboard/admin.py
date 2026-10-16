from django.contrib import admin
from .models import LoginHistory


@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "login_time",
        "ip_address",
    )

    list_filter = ("login_time",)
    search_fields = ("user__username", "ip_address")
    readonly_fields = (
        "user",
        "login_time",
        "ip_address",
        "user_agent",
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
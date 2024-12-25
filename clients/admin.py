from django.contrib import admin

from .models import ClientUser


class ClientUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "last_login",
        "date_joined",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("date_joined",)
    search_fields = ("name", "email", "id")


admin.site.register(ClientUser, ClientUserAdmin)

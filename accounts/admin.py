from django.contrib import admin
from accounts.models import Interest, User
from django.utils.translation import gettext_lazy as _
from accounts.utils.constants import AdminMessages
from django.contrib.messages import SUCCESS
from django.utils.translation import ngettext_lazy


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    readonly_fields = ["id", "password", "date_joined", "last_login"]
    ordering = ("username",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "profile",
                    "first_name",
                    "last_name",
                    "email",
                    "age",
                    "gender",
                    "phone",
                    "address",
                    "following",
                ),
            },
        ),
        (
            _("Status info"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (
            _("Permissions info"),
            {
                "fields": (
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Joined & Login info"), {"fields": ("last_login", "date_joined")}),
    )
    filter_horizontal = ("groups", "user_permissions", "following")
    actions = ["mark_inactive", "mark_active"]

    @admin.action(
        description=AdminMessages.USER_ADMIN_STATUS_INACTIVE_DESCRIPTION.value
    )
    def mark_inactive(self, request, queryset):
        updated = queryset.update(is_active=AdminMessages.STATUS_INACTIVE_BOOL.value)
        message = ngettext_lazy(
            AdminMessages.USER_ADMIN_STATUS_INACTIVE_SUCCESS.value,
            AdminMessages.USER_ADMIN_STATUS_INACTIVE_SUCCESS_PLURAL.value,
            updated,
        ) % {
            "updated": updated,
        }
        self.message_user(
            request,
            message,
            SUCCESS,
        )

    @admin.action(description=AdminMessages.USER_ADMIN_STATUS_ACTIVE_DESCRIPTION.value)
    def mark_active(self, request, queryset):
        updated = queryset.update(is_active=AdminMessages.STATUS_ACTIVE_BOOL.value)
        message = ngettext_lazy(
            AdminMessages.USER_ADMIN_STATUS_ACTIVE_SUCCESS.value,
            AdminMessages.USER_ADMIN_STATUS_ACTIVE_SUCCESS_PLURAL.value,
            updated,
        ) % {
            "updated": updated,
        }
        self.message_user(
            request,
            message,
            SUCCESS,
        )


@admin.register(Interest)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    search_fields = ["user"]
    ordering = ["id"]
    readonly_fields = ["id"]
    fieldsets = (
        (
            _("Interest Details"),
            {
                "fields": (
                    "user",
                    "category",
                    "tag",
                ),
            },
        ),
    )
    filter_horizontal = ["tag", "category"]

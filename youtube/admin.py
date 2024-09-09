from django.contrib.admin import ModelAdmin, register
from youtube.models import Region, Channel, Category, Video, Tag
from django.utils.translation import gettext_lazy as _


@register(Region)
class RegionAdmin(ModelAdmin):
    list_display = ("id", "title")
    search_fields = ["title"]
    ordering = ["id"]
    readonly_fields = ["id"]
    fieldsets = (
        (
            _("Region Details"),
            {
                "fields": (
                    "id",
                    "title",
                ),
            },
        ),
    )


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ("id", "title")
    search_fields = ["title"]
    ordering = ["id"]
    readonly_fields = ["id"]
    fieldsets = (
        (
            _("Tag Details"),
            {
                "fields": (
                    "id",
                    "title",
                ),
            },
        ),
    )


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("id", "title")
    search_fields = ["title"]
    ordering = ["id"]
    readonly_fields = ["id"]
    fieldsets = (
        (
            _("Category Details"),
            {
                "fields": (
                    "id",
                    "title",
                ),
            },
        ),
    )


@register(Channel)
class ChannelAdmin(ModelAdmin):
    list_display = ["id", "title", "subscribers", "video_count", "channel_id"]
    readonly_fields = ["id", "channel_id"]
    ordering = ("id", "title")
    fieldsets = (
        (None, {"fields": ("id", "channel_id")}),
        (
            _("Channel Info"),
            {
                "fields": (
                    "title",
                    "description",
                    "region",
                    "published",
                ),
            },
        ),
        (
            _("Channel Statistics"),
            {
                "fields": (
                    "views",
                    "subscribers",
                    "video_count",
                ),
            },
        ),
    )


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ["id", "title", "channel", "category"]
    search_fields = ("title", "channel__title", "category__title", "tags__title")
    readonly_fields = ["id", "video_id"]
    ordering = ("id", "title")
    fieldsets = (
        (None, {"fields": ("id", "video_id")}),
        (
            _("Video Info"),
            {
                "fields": ("title", "description", "channel"),
            },
        ),
        (
            _("Video Statistics"),
            {
                "fields": (
                    "views",
                    "like",
                ),
            },
        ),
        (
            _("Video Meta Information"),
            {
                "fields": (
                    "tags",
                    "category",
                ),
            },
        ),
    )

    filter_horizontal = ("tags",)

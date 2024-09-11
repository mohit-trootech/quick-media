from django.contrib.admin import *
from meta.models import Post, PostImage, Comment
from django.utils.translation import gettext as _


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ["id", "title", "user"]
    search_fields = ("title", "user__username", "user__first_name")
    readonly_fields = [
        "id",
    ]
    ordering = ("id", "title")
    fieldsets = (
        (None, {"fields": ["id"]}),
        (
            _("Post Info"),
            {
                "fields": ("title", "description", "user"),
            },
        ),
        (
            _("Post Meta Data"),
            {
                "fields": ("like", "saved"),
            },
        ),
    )

    filter_horizontal = ("like", "saved")


@register(PostImage)
class PostImageAdmin(ModelAdmin):
    list_display = ["id", "post__title"]
    search_fields = ("title", "post__title")
    readonly_fields = ["id", "thumbnail_preview"]
    ordering = ["id"]
    fieldsets = (
        (None, {"fields": ["id"]}),
        (
            _("Post Image Info"),
            {
                "fields": (
                    "post",
                    "image",
                ),
            },
        ),
        (
            "Image Preview",
            {"classes": ["collapse"], "fields": ["thumbnail_preview"]},
        ),
    )


@register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ["id", "title", "user", "post"]
    search_fields = (
        "title",
        "user__title",
        "post__title",
    )
    readonly_fields = ["id"]
    ordering = ("id", "title")
    fieldsets = (
        (None, {"fields": ["id"]}),
        (
            _("Comment Info"),
            {
                "fields": ("title", "user", "post"),
            },
        ),
    )

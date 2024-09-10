from django.urls import path
from meta.views import (
    Instagram,
    AjaxUpdate,
    ProfileView,
    InstagramProfileView,
    Facebook,
    FacebookProfileView,
)
from meta.utils.constants import MetaUrls

urlpatterns = [
    path("instagram/", Instagram.as_view(), name=MetaUrls.INSTAGRAM_REVERSE.value),
    path("facebook/", Facebook.as_view(), name=MetaUrls.FACEBOOK_REVERSE.value),
    path(
        "instagram/<str:user>",
        InstagramProfileView.as_view(),
        name=MetaUrls.INSTAGRAM_USERNAME_PROFILE.value,
    ),
    path(
        "facebook/<str:user>",
        FacebookProfileView.as_view(),
        name=MetaUrls.FACEBOOK_USERNAME_PROFILE.value,
    ),
    path(
        "instagram/profile/<int:id>",
        ProfileView.as_view(),
        name=MetaUrls.INSTAGRAM_PROFILE_REVERSE.value,
    ),
    path(
        "ajax_update/",
        AjaxUpdate.as_view(),
        name=MetaUrls.AJAX_UPDATE.value,
    ),
]

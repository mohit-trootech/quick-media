from django.urls import path
from meta.views import Instagram, AjaxUpdateInstagram, ProfileView, InstagramProfileView
from meta.utils.constants import MetaUrls

urlpatterns = [
    path("instagram/", Instagram.as_view(), name=MetaUrls.INSTAGRAM_REVERSE.value),
    path(
        "instagram/<str:user>",
        InstagramProfileView.as_view(),
        name=MetaUrls.INSTAGRAM_USERNAME_PROFILE.value,
    ),
    path(
        "instagram/profile/<int:id>",
        ProfileView.as_view(),
        name=MetaUrls.INSTAGRAM_PROFILE_REVERSE.value,
    ),
    path(
        "ajax_update_instagram/",
        AjaxUpdateInstagram.as_view(),
        name=MetaUrls.AJAX_UPDATE_INSTAGRAM.value,
    ),
]

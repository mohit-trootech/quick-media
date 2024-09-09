from django.urls import path
from youtube.views import YoutubeHomeView, YoutubeRequestHandle, StreamVideo
from youtube.utils.constants import YoutubeUrlsReverse

urlpatterns = [
    path(
        "",
        YoutubeHomeView.as_view(),
        name=YoutubeUrlsReverse.YOUTUBE_HOME_REVERSE.value,
    ),
    path(
        "request_page/",
        YoutubeRequestHandle.as_view(),
        name=YoutubeUrlsReverse.YOUTUBE_REQUEST_REVERSE.value,
    ),
    path(
        "<str:video_id>/",
        StreamVideo.as_view(),
        name=YoutubeUrlsReverse.YOUTUBE_STREAM_VIDEO_REVERSE.value,
    ),
]

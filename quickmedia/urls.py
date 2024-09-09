from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include
from quickmedia.views import IndexView, InfoView
from schema_graph.views import Schema
from quickmedia.utils.constants import INDEX_REVERSE, SCHEMA_REVERSE, INFO_REVERSE
from django.conf.urls.static import static
from quickmedia.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name=INDEX_REVERSE),
    path("info/", InfoView.as_view(), name=INFO_REVERSE),
    path("accounts/", include("accounts.urls")),
    path("youtube/", include("youtube.urls")),
    path("meta/", include("meta.urls")),
    path("schema/", Schema.as_view(), name=SCHEMA_REVERSE),
] + debug_toolbar_urls()

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

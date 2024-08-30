from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include
from quickmedia.views import IndexView
from schema_graph.views import Schema
from quickmedia.utils.constants import INDEX_REVERSE, SCHEMA_REVERSE

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name=INDEX_REVERSE),
    path("schema", Schema.as_view(), name=SCHEMA_REVERSE),
] + debug_toolbar_urls()

from django.views.generic import TemplateView
from quickmedia.utils.constants import INDEX_TEMPLATE, INFO_TEMPLATE


class IndexView(TemplateView):
    template_name = INDEX_TEMPLATE


class InfoView(TemplateView):
    template_name = INFO_TEMPLATE


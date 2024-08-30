from django.views.generic import TemplateView
from quickmedia.utils.constants import INDEX_TEMPLATE


class IndexView(TemplateView):
    template_name = INDEX_TEMPLATE

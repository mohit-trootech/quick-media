from youtube.models import Category


def get_category(request):
    return {"categories": Category.objects.all()}

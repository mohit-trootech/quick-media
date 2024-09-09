from django.template import Library
from accounts.models import User
from meta.utils.constants import ACTIVE, EMPTY_STR

register = Library()


@register.simple_tag(name="post_liked_by_user")
def post_liked_by_user(id, post, *args, **kwargs):
    """
    template tag to check if post liked by a user

    :param user:
    :param post:
    """
    try:
        post.like.get(id=id)
        return ACTIVE
    except User.DoesNotExist:
        return EMPTY_STR


@register.simple_tag(name="post_saved_by_user")
def post_saved_by_user(id, post, *args, **kwargs):
    """
    template tag to check if post liked by a user

    :param user:
    :param post:
    """
    try:
        post.saved.get(id=id)
        return ACTIVE
    except User.DoesNotExist:
        return EMPTY_STR

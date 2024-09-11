from django.template import Library
from accounts.models import User
from meta.utils.constants import ACTIVE, EMPTY_STR, FOLLOWING, FOLLOW

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


@register.simple_tag(name="is_following")
def is_following(user, other_user, *args, **kwargs):
    """
    template tag to check if user is followed

    :param user:
    :param other_user:
    """
    if other_user.following.filter(id=user.id).exists():
        return FOLLOWING
    return FOLLOW


@register.simple_tag(name="get_mutual_friends")
def get_mutual_friends(user, other_user, *args, **kwargs):
    self_following = set(user.following.all())
    other_following = set(other_user.following.all())
    mutual_friends = self_following.intersection(other_following)

    return len(mutual_friends)

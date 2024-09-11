from django.template import Library

register = Library()


@register.simple_tag(name="get_mutual_friends")
def get_mutual_friends(user, other_user, *args, **kwargs):
    self_following = set(user.following.all())
    other_following = set(other_user.following.all())
    mutual_friends = self_following.intersection(other_following)

    return len(mutual_friends)

@register.simple_tag
def call_method(obj, method_name, *args):
    method = getattr(obj, method_name)
    return method(*args)
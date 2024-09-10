from meta.models import Comment, Post, PostImage
from meta.utils.constants import COMMENT, FOLLOWING, Constants
from accounts.models import User
from meta.utils.constants import TITLE, IMAGES, LIKE, SAVED, USER, POST, ID, FOLLOWERS


def get_post_with_id(id: int):
    """
    return post queryset with id

    :param id: int
    """
    return Post.objects.prefetch_related(LIKE, SAVED).get(id=id)


def get_user_object(id: int):
    """
    get user object with id

    :param id: int
    """
    return User.objects.prefetch_related(FOLLOWERS, FOLLOWING).get(id=id)


def get_create_form_data(request):
    """
    format & returb post create for title & images queryset
    """
    return request.POST.get(TITLE), request.FILES.getlist(IMAGES)


def post_object_create(title: str, user):
    """
    create new post & return the same

    :param title: str
    :param user:
    """
    return Post.objects.prefetch_related(IMAGES).create(title=title, user=user)


def create_post_images_object(post, images):
    """
    create post images
    """
    posts = []
    for image in images:
        posts.append(PostImage(post=post, image=image))
    PostImage.objects.bulk_create(posts)


def file_type_check_for_image(images):
    """
    images list

    :param images: _description_
    :return: _description_
    """
    for image in images:
        if not image.content_type in Constants.FILE_TYPE_IMAGE.value:
            raise AssertionError


def check_if_user_already_liked_post(self, id: int) -> bool:
    """
    check if user already liked a post if not create a like else remove the like

    :param id: int
    """
    try:
        post = get_post_with_id(id=id)
        post.like.get(id=self.request.user.id)
        post.like.remove(self.request.user)
        return False
    except User.DoesNotExist:
        return create_user_like(self, post)


def create_user_like(self, post) -> bool:
    """
    create user like for specific post

    :param post:
    """
    post.like.add(self.request.user)
    return True


def check_if_user_saved_post(self, id: int) -> bool:
    """
    check if user already liked a post if not create a like else remove the like

    :param id: int
    """
    try:
        post = get_post_with_id(id=id)
        post.saved.get(id=self.request.user.id)
        post.saved.remove(self.request.user)
        return False
    except User.DoesNotExist:
        return saved_post_for_user(self, post)


def saved_post_for_user(self, post) -> bool:
    """
    create user like for specific post

    :param post:
    """
    post.saved.add(self.request.user)
    return True


def create_post_comment(self, data):
    """
    create post comment

    :param data:
    """
    comment = Comment.objects.select_related(USER, POST).create(
        user=self.request.user,
        title=data.get(COMMENT),
        post=get_post_with_id(id=data.get(ID)),
    )
    return comment


def update_following_list(request, id):
    """
    add or remove user from following list
    """
    try:
        user = get_user_object(id=id)
        request.user.followers.get(id=user.id)
        request.user.followers.remove(user)
    except User.DoesNotExist:
        request.user.followers.add(user)

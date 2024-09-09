from enum import Enum
from django.utils.translation import gettext_noop as _


class MetaModelsConstants(Enum):
    COMMENTS_FK = "comments"
    POSTS_FK = "posts"
    POST_IMAGE_UPLOAD_TO = "posts"
    FOLLOWING = "following"
    FOLLOWERS = "followers"
    POST_IMAGES = "images"
    LIKES = "likes"
    SAVES = "saves"


class TemplateNames(Enum):
    INSTAGRAM_HOME = "instagram/index.html"
    PROFILE_TEMPLATE = "instagram/profile.html"
    POST_CARD_TEMPLATE = "instagram/feeds-card.html"
    HOME_PAGE_TEMPLATE = "instagram/home-page.html"
    COMMENT_CARD_TEMPLATE = "instagram/comment-card.html"


class MetaUrls(Enum):
    INSTAGRAM_REVERSE = "instagram-home"
    INSTAGRAM_USERNAME_PROFILE = "instagram-username-profile"
    INSTAGRAM_PROFILE_REVERSE = "instagram-profile"
    AJAX_UPDATE_INSTAGRAM = "ajax-update-instagram"


class Messages(Enum):
    PROFILE_UPDATE_SUCCESS = _("Profile Updated Successfully")


class Urls(Enum):
    INSTAGRAM_PROFILE = "meta/profile/{id}"


class Constants(Enum):
    FILE_TYPE_IMAGE = ["image/jpg", "image/png", "image/jpeg", "image/webp"]


class Errors(Enum):
    ASSERTION_ERROR_MESSAGE = "Required Image Files Only"


class ContextNames(Enum):
    POSTS = "posts"


# Key Constants
TYPE = "type"
TITLE = "title"
IMAGES = "images"
COMMENT = "comment"
COMMENTS = "comments"
STATUS = "status"
CREATE = "create"
POST = "post"
POSTS = "posts"
LIKE = "like"
SAVED = "saved"
ID = "id"
USER = "user"
FOLLOWING = "following"
ACTIVE = "active"
EMPTY_STR = ""
FOLLOWERS = "followers"
POST_MODAL = "post_modal"

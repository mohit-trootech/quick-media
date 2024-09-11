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
    FACEBOOK_HOME = "facebook/index.html"
    FACEBOOK_PROFILE_TEMPLATE = "facebook/profile.html"
    HOME_FACEBOOK = "facebook/home.html"
class MetaUrls(Enum):
    INSTAGRAM_REVERSE = "instagram-home"
    INSTAGRAM_USERNAME_PROFILE = "instagram-username-profile"
    INSTAGRAM_PROFILE_REVERSE = "instagram-profile"
    AJAX_UPDATE = "ajax-update"
    FACEBOOK_REVERSE = "facebook-home"
    FACEBOOK_USERNAME_PROFILE = "facebook-username-profile"


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
FOLLOW = "follow"
PAGE = "page"
USERS = "users"
USERS_FOLLOW = "users_folow"
SAVED_POSTS = "saved_posts"

# Profile Thumbnail Preview
THUMBNAIL_PREVIEW_TAG = '<img src="{img}" width="540"/>'
THUMBNAIL_PREVIEW_HTML = """<div class="warning" style="color:#000;width: 320px;
        padding: 12px;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: start;
        background: #FEF7D1;
        border: 1px solid #F7C752;
        border-radius: 5px;
        box-shadow: 0px 0px 5px -3px #111;">
        <div class="warning__icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" viewBox="0 0 24 24" height="24" fill="none">
                <path fill="#393a37" d="m13 14h-2v-5h2zm0 4h-2v-2h2zm-12 3h22l-11-19z" style="
        fill: #F7C752;"></path>
            </svg>
        </div>
        <strong>No Post Image Available</strong>
    </div>"""

from enum import Enum
from django.utils.translation import gettext_noop as _


class ModelConstants(Enum):
    INTEREST_FK = "interests"
    PROFILE_UPLOAD_TO = "profile"


class Choices(Enum):
    MALE_CODE = "M"
    FEMALE_CODE = "F"
    MALE_VALUE = _("Male")
    FEMALE_VALUE = _("Female")
    GENDER_CHOICE = ((MALE_CODE, MALE_VALUE), (FEMALE_CODE, FEMALE_VALUE))


class AdminMessages(Enum):
    USER_ADMIN_STATUS_INACTIVE_DESCRIPTION = "Mark Selected Users as Inactive"
    STATUS_INACTIVE_BOOL = False
    STATUS_ACTIVE_BOOL = True
    USER_ADMIN_STATUS_ACTIVE_DESCRIPTION = "Mark Selected Users as Active"
    USER_ADMIN_STATUS_ACTIVE_SUCCESS = "Selected %(updated)d User is Updated to Active"
    USER_ADMIN_STATUS_ACTIVE_SUCCESS_PLURAL = (
        "Selected %(updated)d Users are Updated to Active"
    )
    USER_ADMIN_STATUS_INACTIVE_SUCCESS = "Selected Users is Updated to Inactive"
    USER_ADMIN_STATUS_INACTIVE_SUCCESS_PLURAL = (
        "Selected %(updated)d Users are Updated to Inactive"
    )


class Templates(Enum):
    PROFILE_TEMPLATE = "accounts/profile.html"
    LOGIN_TEMPLATE = "accounts/login.html"
    REGISTER_TEMPLATE = "accounts/register.html"


class Forms(Enum):
    UPDATE_FORM_PLACEHOLDER = {
        "profile": "Update Your First Name",
        "first_name": "Update Your Last Name",
        "last_name": "Update Your Last Name",
        "email": "Update Email",
        "age": "Update Age",
        "gender": "Update Gender",
        "phone": "Update Phone",
        "address": "Update Address",
    }
    SIGNUP_FORM_PLACEHOLDER = {
        "first_name": "Enter Your First Name",
        "last_name": "Enter Your Last Name",
        "email": "Choose Email",
        "username": "Choose Username",
    }
    LOGIN_FORM_PLACEHOLDER = {
        "username": "Enter Your Username",
        "password": "Enter Your Password",
    }
    SIGNUP_FORM_HELP_TEXT = {
        "email": "Email is Required Field",
        "username": "Username is Required Field",
    }
    LOGIN_FORM_HELP_TEXT = {
        "username": "Username is Required",
        "password": "Password is Required",
    }
    FORM_CONTROL = "form-control"
    FORM_SELECT = "form-select"


class Urls(Enum):
    PROFILE_REVERSE = "profile"
    LOGOUT_REVERSE = "logout"
    LOGIN_REVERSE = "login"
    REGISTER_REVERSE = "register"
    INDEX_REVERSE = "index"
    UPDATE_PROFILE_SUCCESS = "/accounts/profile/{id}"


class Messages(Enum):
    PROFILE_UPDATE_SUCCESS = _("Profile Updated Successfully")
    LOGIN_SUCCESS = _("User Logged in Successfully")
    SIGNUP_SUCCESS = _("User Registered Successfully")
    LOGOUT_SUCCESS = _("User Logged Out")
    LOGIN_ERROR = _(
        "Username or Password is Incorrect Please Try Again with Correct Credentials"
    )
    PASSWORD_NOT_MATCH = _("Password Does Not Match")


# Random Constants
PASSWORD1 = "password1"
PASSWORD2 = "password2"
USERNAME = "username"
PASSWORD = "password"

# Profile Thumbnail Preview
THUMBNAIL_PREVIEW_TAG = '<img src="{img}" width="320"/>'
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
        <strong>No Profile Image Available</strong>
    </div>"""

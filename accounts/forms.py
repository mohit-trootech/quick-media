from ast import For
from django.forms import (
    ModelForm,
    ClearableFileInput,
    NumberInput,
    EmailInput,
    TextInput,
    Form,
    PasswordInput,
    CharField,
    Select,
)
from accounts.models import User
from accounts.utils.constants import Forms


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "profile",
            "first_name",
            "last_name",
            "email",
            "age",
            "gender",
            "phone",
            "address",
        ]
        widgets = {}
        for field in fields:
            if not field == "gender":
                input_option = TextInput
                if field == "profile":
                    input_option = ClearableFileInput
                elif field == "age" or field == "phone":
                    input_option = NumberInput
                elif field == "email":
                    input_option = EmailInput
                elif field == "gender":
                    input_option = Select
                widgets[field] = input_option(
                    attrs={
                        "class": Forms.FORM_CONTROL.value,
                        "placeholder": Forms.UPDATE_FORM_PLACEHOLDER.value[field],
                    }
                )
            else:
                widgets[field] = Select(
                    attrs={
                        "class": Forms.FORM_SELECT.value,
                        "placeholder": Forms.UPDATE_FORM_PLACEHOLDER.value[field],
                    }
                )


class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]
        widgets = {}
        help_texts = {}
        for field in fields:
            input_option = TextInput
            if field == "email":
                input_option = EmailInput
            widgets[field] = input_option(
                attrs={
                    "class": Forms.FORM_CONTROL.value,
                    "placeholder": Forms.SIGNUP_FORM_PLACEHOLDER.value[field],
                }
            )
            if field in ["username", "email"]:
                help_texts[field] = Forms.SIGNUP_FORM_HELP_TEXT.value[field]


class UserLoginForm(Form):
    username = CharField(
        required=True,
        max_length=30,
        widget=TextInput(
            attrs={
                "class": Forms.FORM_CONTROL.value,
                "placeholder": Forms.LOGIN_FORM_PLACEHOLDER.value["username"],
            }
        ),
        help_text=Forms.LOGIN_FORM_HELP_TEXT.value["username"],
    )
    password = CharField(
        required=True,
        widget=PasswordInput(
            attrs={
                "class": Forms.FORM_CONTROL.value,
                "placeholder": Forms.LOGIN_FORM_PLACEHOLDER.value["password"],
                "autocomplete": "password",
            }
        ),
        help_text=Forms.LOGIN_FORM_HELP_TEXT.value["password"],
    )

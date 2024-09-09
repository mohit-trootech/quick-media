from django.views.generic import UpdateView, FormView, View
from accounts.utils.constants import (
    PASSWORD,
    USERNAME,
    Messages,
    Urls,
    Templates,
    PASSWORD1,
    PASSWORD2,
)
from accounts.forms import ProfileUpdateForm, UserLoginForm, UserRegisterForm
from accounts.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib.messages import info
from dotenv import dotenv_values
from login_required import login_not_required
from django.urls import reverse_lazy
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

config = dotenv_values(".env")


class ProfileView(UpdateView):
    template_name = Templates.PROFILE_TEMPLATE.value
    form_class = ProfileUpdateForm
    model = User

    def get_object(self):
        """
        return the request user in object always
        """
        return User.objects.get(id=self.request.user.pk)

    def get_success_url(self) -> str:
        """
        returns success url if form is valid
        """
        info(self.request, Messages.PROFILE_UPDATE_SUCCESS.value)
        return Urls.UPDATE_PROFILE_SUCCESS.value.format(id=self.request.user.pk)


@login_not_required
class LoginView(FormView):
    template_name = Templates.LOGIN_TEMPLATE.value
    form_class = UserLoginForm
    success_url = reverse_lazy(Urls.INDEX_REVERSE.value)

    def form_valid(self, form):
        """
        login form handle, user will log in if details form is valid else if user not exist return form_invalid

        :param form: _description_
        :return: _description_
        """
        user = authenticate(
            username=form.cleaned_data[USERNAME],
            password=form.cleaned_data[PASSWORD],
        )
        if not user:
            form.add_error(None, Messages.LOGIN_ERROR.value)
            return super().form_invalid(form)
        login(self.request, user)
        info(self.request, Messages.LOGIN_SUCCESS.value)
        return super().form_valid(form)


@login_not_required
class RegisterView(FormView):
    template_name = Templates.REGISTER_TEMPLATE.value
    form_class = UserRegisterForm
    success_url = reverse_lazy(Urls.LOGIN_REVERSE.value)

    def form_valid(self, form):
        """
        registration form handle, user signed up if form_valid else if password not match user already exist or password valiadtion return form_invalid
        """
        try:
            password1 = self.request.POST.get(PASSWORD1)
            password2 = self.request.POST.get(PASSWORD2)
            validate_password(password1)  #  type: ignore
            if not password1 == password2:
                form.add_error(None, Messages.PASSWORD_NOT_MATCH.value)
                return super().form_invalid(form)
            user = form.save(commit=False)
            user.set_password(password1)
            user.save()
            info(self.request, Messages.SIGNUP_SUCCESS.value)
            return super().form_valid(form)
        except ValidationError as ve:
            form.add_error(None, ve)
            return super().form_invalid(form)


class LogoutView(View):

    def get(self, request):
        logout(request)
        info(request, Messages.LOGOUT_SUCCESS.value)
        return redirect("/")

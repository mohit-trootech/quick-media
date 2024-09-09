from django.urls import path
from accounts.views import ProfileView, LogoutView, RegisterView, LoginView
from accounts.utils.constants import Urls

urlpatterns = [
    path("profile/<int:id>", ProfileView.as_view(), name=Urls.PROFILE_REVERSE.value),
    path("login/", LoginView.as_view(), name=Urls.LOGIN_REVERSE.value),
    path("register/", RegisterView.as_view(), name=Urls.REGISTER_REVERSE.value),
    path("logout/", LogoutView.as_view(), name=Urls.LOGOUT_REVERSE.value),
]

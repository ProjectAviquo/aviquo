from django.urls import path
from django.conf import settings

from .email_sender import CustomPasswordResetView
from .views import opportunity_list, SignUp, home, Login

urlpatterns = [
    path("home/", home, name="home"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("opportunity/", opportunity_list, name="opportunity"),
    path("password_reset/", CustomPasswordResetView.as_view(),
             name="password_reset"),
]
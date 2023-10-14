from django.urls import path
from django.conf import settings

from .email_sender import CustomPasswordResetView
from .views import ForumView, OpportunityView, SignUp, home, profile, clogout, waitlist


urlpatterns = [
    path("", home, name="home"),
    path("Waitlist/", waitlist, name="waitlist"),
]

if settings.DEBUG:
    urlpatterns += [
        path('logout/', clogout, name='logout'),
        path("signup/", SignUp.as_view(), name="signup"),
        # path("account/login/", LogIn.as_view(), name="login"),
        path("opportunity/", OpportunityView, name="opportunity"),
        path("forum/", ForumView, name="forum"),
        path("profile/", profile, name="profile"),
        path("password_reset/", CustomPasswordResetView.as_view(),
             name="password_reset"),
        # path("Waitlist/", waitlist, name="waitlist")
    ]

from django.urls import path

from .email_sender import CustomPasswordResetView
from .views import ForumView, OpportunityView, SignUp, WaitlistView, home, profile, clogout


urlpatterns = [
    path("", home, name="home"),
    path('logout', clogout, name='logout'),
    path("signup/", SignUp.as_view(), name="signup"),
    path("opportunity/", OpportunityView, name="opportunity"),
    path("waitlist/", WaitlistView.as_view(), name="waitlist"),
    path("forum/", ForumView, name="forum"),
    path("profile/", profile, name="profile"),
    path("password_reset/", CustomPasswordResetView.as_view(), name="password_reset"),
]

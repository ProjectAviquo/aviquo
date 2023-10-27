from django.urls import path
from django.conf import settings

from .email_sender import CustomPasswordResetView
from .views import ForumView, OpportunityView, SignUp, home, profile, clogout, waitlist, profilee


urlpatterns = [
    path("", home, name="home"),
    path("waitlist/", waitlist, name="waitlist"),
    path('logout/', clogout, name='logout'),
    path("signup/", SignUp.as_view(), name="signup"),
    path("opportunity/", OpportunityView, name="opportunity"),
    path("forum/", ForumView, name="forum"),
    path('profile/<str:username>/', profile, name='profile'),
    path('profile/', profilee, name='profilee'),
    path("password_reset/", CustomPasswordResetView.as_view(),
             name="password_reset"),
]



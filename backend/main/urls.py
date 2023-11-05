from django.urls import path
from django.conf import settings

from .email_sender import CustomPasswordResetView
from .views import ForumView, OpportunityView, SignUp, home, profile, clogout, waitlist, profilee, Login,  follow_opportunity, delete_forum, navbar, follow_user, edit_profile

urlpatterns = [
    path("", home, name="home"),
    path("waitlist/", waitlist, name="waitlist"),
    path('logout/', clogout, name='logout'),
    path("signup/", SignUp.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("opportunity/", OpportunityView, name="opportunity"),
    path("forum/", ForumView, name="forum"),
    path('profile/<str:username>/', profile, name='profile'),
    path('profile/', profilee, name='profilee'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('follow-opportunity/',  follow_opportunity, name=' follow_opportunity'),
    path('delete_forum/<int:forum_id>/', delete_forum, name='delete_forum'),
    path('follow-user/', follow_user, name='follow_user'),
    path("password_reset/", CustomPasswordResetView.as_view(),
             name="password_reset"),
    path("navbar/", navbar, name="navbar") #testing dont TODO: remove later
]
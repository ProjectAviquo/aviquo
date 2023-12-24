"""Main views"""
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.http import JsonResponse
from rest_framework import generics

from .models import Forum, Opportunity, User, Waitlist, Tag
from .serializers import ForumSerializer, WaitlistSerializer
from .forms import (
    EditProfileForm,
    AddWaitlistForm,
    AddForumForm,
    CustomAuthForm,
    CustomUserCreationForm,
)
from core.settings import DEBUG

import os


def home(request):
    """Home view. Show username"""
    if request.user.is_authenticated:
        return redirect("profile", username=request.user.username)
    return render(request, "home.html", {})


def waitlist(request):
    """Waitlist + form"""
    if request.method == "POST":
        form = AddWaitlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("waitlist")
    else:
        form = AddWaitlistForm()
    return render(request, "waitlist/waitlist.html", {"form": form})


def clogout(request):
    """Log out user"""
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")


@login_required
def profile(request, username):
    """Get profile"""
    user = get_object_or_404(User, username=username)
    return render(request, "users/profile.html", {"user": user, "ouser": request.user})


@login_required
def following(request, username):
    """Get follwing"""
    user = get_object_or_404(User, username=username)
    return render(
        request, "users/following.html", {"user": user, "ouser": request.user}
    )


@login_required
def followers(request, username):
    """Get followers"""
    user = get_object_or_404(User, username=username)
    return render(
        request, "users/followers.html", {"user": user, "ouser": request.user}
    )


@login_required
def edit_profile(request):
    """Edit profile + form"""

    user = request.user
    # Display the profile form to everyone
    form = EditProfileForm(instance=user)
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            # form.instance.bio = bio
            # form.instance.profile_image = pic
            form.save()

            return redirect("profile", username=user.username)
    return render(request, "users/profile_edit.html", {"user": user, "form": form})


@login_required
def profilee(request):
    """Self profile"""
    return redirect("profile", request.user.username)


@login_required
def OpportunityView(request):
    """View OPPS"""
    opportunities = Opportunity.objects.all()
    tags = Tag.objects.all()
    return render(
        request,
        "lists/opportunity_list.html",
        {"opportunities": opportunities, "all_tags": tags},
    )


@login_required
def ForumView(request):
    """View forums"""
    forums = Forum.objects.all()
    user = request.user
    if request.method == "POST":
        form = AddForumForm(request.POST)
        if form.is_valid():
            # Create a new Forum instance but don't save it yet
            new_forum = form.save()

            new_forum.user = user
            request.user.created_forums.add(new_forum)
            print(new_forum.user.username)
            new_forum.save()
            return redirect("forum")

    else:
        form = AddForumForm()
    return render(request, "lists/forum_list.html", {"forums": forums, "form": form})


class SignUp(CreateView):
    """Signup view + form"""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class Login(LoginView):
    """Login view + form"""

    template_name = "accounts/login.html"


def delete_forum(request, forum_id):
    """Delete a forum if author"""
    try:
        forum = Forum.objects.get(pk=forum_id)
        # Check if the user is the author
        if request.user == forum.user:
            forum.delete()

    except Forum.DoesNotExist:
        pass

    # Redirect to the page that the request originated from
    return redirect(request.META.get("HTTP_REFERER", "/"))


def unfollow_user(request, user_id):
    """Unfollow user if follower"""
    try:
        user = User.objects.get(pk=user_id)
        # Check if the user is the author
        request.user.followers.remove(user)
        user.following.remove(request.user)

    # TODO what
    except Forum.DoesNotExist:
        pass

    # Redirect to the page that the request originated from
    return redirect(request.META.get("HTTP_REFERER", "/"))


def follow_user(request):
    """Folow user"""
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        action = request.POST.get("action")
        user = request.user

        # Retrieve the opportunity instance
        user_to_follow = User.objects.get(id=user_id)

        if action == "follow":
            user.following.add(user_to_follow)
            user_to_follow.followers.add(user)
            response = "followed"
        else:
            print(user_to_follow.username)
            print(user.username)
            user.following.remove(user_to_follow)
            user_to_follow.followers.remove(user)
            response = "unfollowed"

        return JsonResponse(response, safe=False)

    return JsonResponse({}, status=400)


def follow_opportunity(request):
    """Follow OPP"""
    if request.method == "POST":
        opportunity_id = request.POST.get("opportunity_id")
        action = request.POST.get("action")
        user = request.user

        # Retrieve the opportunity instance
        opportunity = Opportunity.objects.get(id=opportunity_id)

        if action == "follow":
            user.followed_opps.add(opportunity)
            response = "followed"
        else:
            user.followed_opps.remove(opportunity)
            response = "unfollowed"

        return JsonResponse(response, safe=False)

    return JsonResponse({}, status=400)

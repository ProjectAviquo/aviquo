from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect, render,  get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework import generics
from .models import Forum, Opportunity, User, Waitlist
from .serializers import ForumSerializer, WaitlistSerializer
from django.http import JsonResponse
from .forms import EditProfileForm, AddWaitlistForm, AddForumForm, CustomAuthForm, CustomUserCreationForm


def home(request):
    if request.user.is_authenticated:
       return redirect("profile", username=request.user.username)
    return render(request, "home.html", {})

def waitlist(request):
    if request.method == "POST":
        form = AddWaitlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("waitlist")
    else:
        form = AddWaitlistForm()
    return render(request, "waitlist/landing_page.html", {"form":form})
def clogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    form = EditProfileForm(instance=user)  # Display the profile form to everyone
    if request.user.username == username:
        if request.method == "POST":
            form = EditProfileForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
            return redirect("profile", username=user.username)
        return render(request, "users/profile.html", {"user": user, "form": form})
    else:
        return render(request, "users/profile.html", {"user": user})

@login_required
def profilee(request):
    return redirect("profile", request.user.username)

@login_required
def OpportunityView(request):
    opportunities = Opportunity.objects.all()

    return render(request, "lists/opportunity_list.html", {"opportunities": opportunities})


@login_required
def ForumView(request):
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
    return render(request, "lists/forum_list.html", {"forums": forums, "form":form})



class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pridemonthmode'] = False
        return context

class Login(LoginView):
    template_name="accounts/login.html"

def delete_forum(request, forum_id,):
    try:
        forum = Forum.objects.get(pk=forum_id)
        # Check if the user is the author
        if request.user == forum.user:
            forum.delete()

    except Forum.DoesNotExist:
        pass

    # Redirect to the page that the request originated from
    return redirect(request.META.get('HTTP_REFERER', '/')) 

def follow_opportunity(request):
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
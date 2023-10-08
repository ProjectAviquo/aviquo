from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework import generics
from .models import Forum, Opportunity, User, Waitlist
from .serializers import ForumSerializer, WaitlistSerializer


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

class AddWaitlistForm(forms.ModelForm):
    class Meta:
        model = Waitlist
        fields = ["email"]

class AddForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ["topic", "description"]

def home(request):
    # return redirect("waitlist")
    if request.user.is_authenticated:
       return redirect("profile")
    return render(request, "home.html", {})

def waitlist(request):
    if request.method == "POST":
        form = AddWaitlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("waitlist")

    else:
        form = AddWaitlistForm()
    return render(request, "Waitlist/landing_page.html", {"form":form})
def clogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")

@login_required
def profile(request):
    user = request.user

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = EditProfileForm(instance=user)

    return render(request, "users/profile.html", {"user": user, "form": form})


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
            new_forum = form.save(commit=False)
            
            # Set the username field of the forum to the user's username
            new_forum.username = user.username
            
            # Save the forum object with the updated username
            new_forum.save()
            
            return redirect("forum")

    else:
        form = AddForumForm()
    return render(request, "lists/forum_list.html", {"forums": forums, "form":form})

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Make the email field required
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# class ForumView(generics.CreateAPIView):
#     queryset = Forum.objects.all()
#     serializer_class = ForumSerializer


class WaitlistView(generics.CreateAPIView):
    queryset = Waitlist.objects.all
    serializer_class = WaitlistSerializer

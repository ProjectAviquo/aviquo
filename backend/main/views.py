from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Opportunity, Tag, Category
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Count


# Your home view
def home(request):
    return render(request, "home.html", {})


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy(
        "opportunity"
    )  # Redirect to the opportunity list after signup
    template_name = "accounts/signup.html"

    def form_valid(self, form):
        # Save the new user first
        self.object = form.save()
        # Then log the user in
        login(self.request, self.object)
        # Then redirect to the desired URL (in this case, 'opportunity')
        return redirect(self.success_url)


class Login(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        return reverse_lazy("opportunity")  # Redirect here after a successful login


# Your OpportunityView remains unchanged

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Opportunity


@login_required
def opportunity_list(request):
    all_tags = Tag.objects.all()
    active_tags = request.GET.getlist("tags")

    opportunities = Opportunity.objects.all()

    # This block of code should not be needed as we are going to handle the tags through 'tags' parameter
    # if 'add_tag' in request.GET:
    #     tag_to_add = request.GET['add_tag']
    #     if tag_to_add not in active_tags:
    #         active_tags.append(tag_to_add)

    # This block of code should not be needed as we are going to handle the tags through 'tags' parameter
    # if 'remove_tag' in request.GET:
    #     tag_to_remove = request.GET['remove_tag']
    #     if tag_to_remove in active_tags:
    #         active_tags.remove(tag_to_remove)

    # Handle bookmarking only when 'bookmark_opportunity' is in the GET parameters and not on every request
    if "bookmark_opportunity" in request.GET:
        opportunity_id = request.GET["bookmark_opportunity"]
        opportunity = Opportunity.objects.get(id=opportunity_id)
        if request.user in opportunity.bookmarked_users.all():
            opportunity.bookmarked_users.remove(request.user)
        else:
            opportunity.bookmarked_users.add(request.user)
        return redirect(
            "opportunity"
        )  # Redirect to itself to prevent re-bookmarking/undo-bookmarking on refresh

    # Toggle showing bookmarked opportunities
    if "show_bookmarked" in request.GET:
        request.session["show_bookmarked_toggle"] = not request.session.get(
            "show_bookmarked_toggle", False
        )
        return redirect(
            "opportunity"
        )  # Redirect to itself to prevent toggling state on refresh

    # Filter opportunities based on bookmarked or not
    opportunities = Opportunity.objects.all()
    if request.session.get("show_bookmarked_toggle"):
        opportunities = opportunities.filter(bookmarked_users=request.user)

    if active_tags:
        for tag in active_tags:
            opportunities = opportunities.filter(tags__name=tag)  # Filter for each tag
        opportunities = opportunities.distinct()

    context = {
        "all_tags": all_tags,
        "active_tags": active_tags,
        "opportunities": opportunities,
    }
    return render(request, "lists/opportunity_list.html", context)


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class Login(LoginView):
    template_name = "accounts/login.html"

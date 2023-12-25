from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Opportunity, Tag
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Count



# Your home view
def home(request):
    return render(request, "home.html", {})

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("opportunity")  # Redirect to the opportunity list after signup
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
        return reverse_lazy('opportunity')  # Redirect here after a successful login

# Your OpportunityView remains unchanged

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Opportunity

@login_required
def opportunity_list(request):
    all_tags = Tag.objects.all()
    active_tags = request.GET.getlist('tags')

    if 'add_tag' in request.GET:
        tag_to_add = request.GET['add_tag']
        if tag_to_add not in active_tags:
            active_tags.append(tag_to_add)


    # Handle bookmarking
    if 'bookmark_opportunity' in request.GET:
        opportunity_id = request.GET['bookmark_opportunity']
        opportunity = Opportunity.objects.get(id=opportunity_id)
        if request.user in opportunity.bookmarked_users.all():
            opportunity.bookmarked_users.remove(request.user)
        else:
            opportunity.bookmarked_users.add(request.user)

    # Toggle showing bookmarked opportunities
    if 'show_bookmarked' in request.GET:
        if 'show_bookmarked_toggle' in request.session:
            del request.session['show_bookmarked_toggle']
        else:
            request.session['show_bookmarked_toggle'] = True

    # Filter opportunities based on bookmarked or not
    if 'show_bookmarked_toggle' in request.session:  # If showing only bookmarked opportunities, start with them
        opportunities = Opportunity.objects.filter(bookmarked_users=request.user)
    else:
        opportunities = Opportunity.objects.all()  # Pick all or only bookmarked ones to start with

    if active_tags:
        opportunities = [opp for opp in opportunities if set(active_tags).issubset(opp.tags.values_list('name', flat=True))]

    context = {
        'all_tags': all_tags,
        'active_tags': active_tags,
        'opportunities': opportunities,
    }

    return render(request, 'lists/opportunity_list.html', context)

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

class Login(LoginView):
    template_name="accounts/login.html"

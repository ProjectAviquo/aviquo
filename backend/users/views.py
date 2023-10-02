from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Opportunity, Forum, Waitlist
from rest_framework import generics
from .serializers import OpportunitySerializer, ForumSerializer, WaitlistSerializer
from django import forms
from django.shortcuts import render, redirect

# from django.contrib.auth import get_user_model
# User = get_user_model()

# Create your views here.
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

def home(request):
    return render(request, 'home.html', {})

@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfileForm(instance=user)

    return render(request, 'users/profile.html', {'user': user, 'form': form})

@login_required
def OpportunityView(request):
     data = Opportunity.objects.all()

    # Render the template with the data
     return render(request, 'oppDetails.html', {'data': data})



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Make the email field required

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class ForumView(generics.CreateAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer



class WaitlistView(generics.CreateAPIView):
    queryset = Waitlist.objects.all
    serializer_class  = WaitlistSerializer

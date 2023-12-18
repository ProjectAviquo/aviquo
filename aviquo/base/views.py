"""
Views for the Base app
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import RegisterForm


# Authentication
def signup(request: HttpRequest) -> HttpResponse:
    """Sign up view"""
    match request.method:
        case "GET":
            form = RegisterForm
            return render(request, "")
        case _:
            return redirect("/signup")

"""
Views for the Base app
"""
# pylint: disable=unused-variable

import logging
from json import dumps
from typing import Union

from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .forms import RegisterForm
from .models import User

logger = logging.getLogger(__name__)


# Authentication
def signup(request: HttpRequest) -> Union[HttpResponse, HttpResponseBadRequest]:
    """Sign up view and form handler"""
    match request.method:
        case "GET":
            form = RegisterForm
            return render(request, "")

        case "POST":
            form_data = RegisterForm(request.POST)
            if form_data.is_valid():
                user: User = form_data.save()
                logger.info(
                    "New user: %s! Now at %d Gemosians!",
                    user.username,
                    User.objects.count(),
                )
                return redirect("/login?err=9")
            else:
                logger.warning(
                    "Bad data:\n%s",
                    dumps(
                        dict(form_data.data),
                        indent=2,
                    ),
                )
                return HttpResponseBadRequest()

        case _:
            return redirect("/signup")

"""API Views"""
import random
from typing import Any

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Forum, Opportunity, Tag, User, Waitlist
from rest_framework import generics, permissions, viewsets
from rest_framework_api_key.models import APIKey

from .serializers import ForumSerializer, OpportunitySerializer, \
    TagSerializer, UserSerializer, WaitlistSerializer


class BaseViewSet(viewsets.ModelViewSet):
    """Base view for the REST API"""
    model, serializer_class, queryset = None, None, None

    def get_queryset(self):
        """Gets the queryset, filtered"""
        field_names = [field.name for field in self.model._meta.get_fields()]

        filter_params = {
            key: self.request.query_params.get(key) for key in field_names
        }

        return_dict = {
            key: val for key, val in filter_params.items() if val is not None
        }

        return self.model.objects.filter(**return_dict)

class UserViewSet(BaseViewSet):
    """User viewset.
    Model - User
    Serializer - UserSerializer
    Queryset - all"""
    model = User
    serializer_class = UserSerializer
    queryset = model.objects.all()


class RegistrationAPIView(generics.CreateAPIView):
    """Registration viewset.
    Serializer - UserSerializer
    Queryset - all
    Perms - Any"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)


class ForumViewSet(BaseViewSet):
    """Forum viewset.
    Model - Forum
    Serializer - ForumSerializer
    Queryset - all"""
    model = Forum
    serializer_class = ForumSerializer
    queryset = model.objects.all()


class OpportunityViewSet(BaseViewSet):
    """Opportunity viewset.
    Model - Opportunity
    Serializer - OpportunitySerializer
    Queryset - all"""
    model = Opportunity
    serializer_class = OpportunitySerializer
    queryset = model.objects.all()


class TagViewSet(BaseViewSet):
    """Tag viewset.
    Model - Tag
    Serializer - TagSerializer
    Queryset - all"""
    model = Tag
    serializer_class = TagSerializer
    queryset = model.objects.all()


class WaitlistViewSet(BaseViewSet):
    """Waitlist viewset.
    Model - Waitlist
    Serializer - WaitlistSerializer
    Queryset - all"""
    model = Waitlist
    serializer_class = WaitlistSerializer
    queryset = model.objects.all()


@csrf_exempt
def gen_api_key(request):
    """Generate an API key"""
    if request.headers.get("Referer") == "http://localhost:3000/":
        name = "demo-key-gen-" + str(random.randint(100, 20000))

        _, key = APIKey.objects.create_key(name=name)
        response_data = {"key": key}

        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "Unauthorized"}, status=401)

"""Serializers"""
from rest_framework import serializers
from .models import Forum, Opportunity, User, Waitlist


class ForumSerializer(serializers.ModelSerializer):
    """Forum serializer. All fields"""

    class Meta:
        model = Forum
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """User serializer. All fields"""

    class Meta:
        model = User
        fields = "__all__"


class OpportunitySerializer(serializers.ModelSerializer):
    """Opportunity serializer. All fields"""

    class Meta:
        model = Opportunity
        fields = "__all__"


class WaitlistSerializer(serializers.ModelSerializer):
    """Waitlist serializer. All fields"""

    class Meta:
        model = Waitlist
        fields = "__all__"

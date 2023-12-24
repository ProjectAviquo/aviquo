"""
REST API Serializer
"""

from main.models import Forum, Opportunity, Tag, User, Waitlist
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    """Base model serializer for the other serializers"""

    class Meta:
        """Meta class"""

        abstract = True
        fields = "__all__"


class UserSerializer(BaseSerializer):
    """User serializer"""

    class Meta(BaseSerializer.Meta):
        """Meta class for fields"""

        model = User
        # fields = ('id', 'username', 'email', 'password')
        # extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    """Login serializer"""

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class ForumSerializer(BaseSerializer):
    """Forum serializer"""

    class Meta(BaseSerializer.Meta):
        """Meta class"""

        model = Forum


class OpportunitySerializer(BaseSerializer):
    """Opportunity serializer"""

    class Meta(BaseSerializer.Meta):
        """Meta class"""

        model = Opportunity


class TagSerializer(BaseSerializer):
    """Tag serializer"""

    class Meta(BaseSerializer.Meta):
        """Meta class"""

        model = Tag


class WaitlistSerializer(serializers.ModelSerializer):
    """Waitlist serializer"""

    class Meta:
        """Meta class"""

        model = Waitlist
        fields = "__all__"

"""REST API Serializer"""
from rest_framework import serializers
from main.models import Forum, Opportunity, Tag, User, Waitlist


class BaseSerializer(serializers.ModelSerializer):
    """Base serializer for the API.
    Parent of other ones"""
    class Meta:
        """Meta class for fields"""
        abstract = True
        fields = "__all__"


class UserSerializer(BaseSerializer):
    """Serializer for users.
    User model"""
    class Meta(BaseSerializer.Meta):
        """Meta class for fields"""
        model = User
        # fields = ('id', 'username', 'email', 'password')
        # extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    """Serializer for login
    Username and password"""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class ForumSerializer(BaseSerializer):
    """Forum serializer.
    Forum model"""
    class Meta(BaseSerializer.Meta):
        """Meta class for fields"""
        model = Forum


class OpportunitySerializer(BaseSerializer):
    """Opportunity serializer.
    Opportunity Model"""
    class Meta(BaseSerializer.Meta):
        """Meta class for fields"""
        model = Opportunity


class TagSerializer(BaseSerializer):
    """Tag serializer.
    Tag model"""
    class Meta(BaseSerializer.Meta):
        """Meta class for fields"""
        model = Tag


class WaitlistSerializer(serializers.ModelSerializer):
    """Waitlist serializer.
    Waitlist model and all fields"""
    class Meta:
        """Meta class for fields"""
        model = Waitlist
        fields = "__all__"

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models





class Tag(models.Model):
    """Global list of tags/keywords applicable to opportunities.

    Examples: scholarship, extracurricular activity, etc.
    """

    name = models.TextField(
        unique=True, max_length=50, verbose_name="Tag", help_text="scholarship, extracurricular activity, etc."
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

    def clean(self):
        if not self.name.strip():
            raise ValidationError("Tag cannot be empty")


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"





class Opportunity(models.Model):
    name = models.TextField(max_length=200, verbose_name="Opportunity", help_text="Opportunity name/title")
    description = models.TextField(
        max_length=4000, verbose_name="Description", help_text="Detailed description of the opportunity"
    )
    URL = models.URLField(max_length=200, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Opportunities"

    def list_tags(self):
        tags = self.tags.order_by("name")
        return " " + ", ".join([tag.name for tag in tags]) if tags else ""


class Waitlist(models.Model):
    email = models.EmailField(max_length=320, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.email)

    class Meta:
        ordering = ["-date_created"]

class User(AbstractUser):
    # other usable fields from AbstractUser:
    #  username, first_name, last_name, email, is_staff, is_active, date_joined, last_login
    bio = models.TextField(verbose_name="Bio", max_length=4000, blank=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True, null=True)

    following =  models.ManyToManyField('self', blank=True, symmetrical=False, related_name="following_set")
    followers =  models.ManyToManyField('self', blank=True, symmetrical=False, related_name="followers_set")

    followed_opps = models.ManyToManyField(Opportunity, blank=True)
    created_forums = models.ManyToManyField('Forum', related_name='creator', blank=True)
    def __str__(self):
        return str(self.id)

    def get_full_name(self) -> str:
        return super().get_full_name()
    

class Forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    parent_post = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["date_created"]
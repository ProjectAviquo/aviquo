"""Main admin"""
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Forum, Opportunity, Tag, User, Waitlist


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin user model"""
    list_display = ("id", "username")


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    """Admin display for opportunities"""
    list_display = ("name", "URL", "all_tags")
    search_fields = ("name", "URL", "description")
    list_per_page = 25
    list_filter = ("tags",)
    # ordering = ('-created_at',)

    @admin.display(description="Tags")
    def all_tags(self, obj):
        """Return tags"""
        return obj.list_tags()


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    """Admin display for forum"""
    list_display = ("topic", "user")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin display for tags"""
    list_display = ("name", "tag_count")
    search_fields = ("name",)
    list_per_page = 25
    # list_filter = ("tags",)

    @admin.display(description="# of opportunities with this tag")
    def tag_count(self, obj):
        """How many opps with tag"""
        qs = Opportunity.objects.filter(tags__name__iexact=obj.name)
        return qs.count()


@admin.register(Waitlist)
class WaitlistAdmin(admin.ModelAdmin):
    """Waitlist admin display"""
    list_display = ("email", "date_created")
    search_fields = ("email",)
    list_per_page = 25
    list_filter = ("date_created",)
    date_hierarchy = "date_created"
    fields = ("email", "date_created")
    readonly_fields = ("date_created",)


admin.site.unregister(Group)

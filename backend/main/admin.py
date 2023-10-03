from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Forum, Opportunity, Tag, User, Waitlist


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    pass


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Waitlist)
class WaitlistAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)

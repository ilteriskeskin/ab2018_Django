from django.contrib import admin
from election.profile.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_staff', 'is_superuser', 'created_at')

admin.site.register(UserProfile, UserProfileAdmin)
from django.contrib import admin

from .models import Profile, Avatar


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'fullName']
    list_display_links = ['fullName']
    search_fields = ['fullName']
    list_filter = ['fullName']
    fields = [
        'user',
        'name',
        'email',
        'phone',
        'fullName',
    ]


@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ['src', 'alt']
    list_display_links = ['src']
    fields = [
        'avatar',
        'src',
        'alt',
    ]

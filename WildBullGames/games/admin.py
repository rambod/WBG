# games/admin.py

from django.contrib import admin
from .models import Game, Review, Submission, Tag, Screenshot, Category,Platform


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'developer', 'release_date')
    list_filter = ('developer', 'release_date')
    search_fields = ('title', 'developer__username')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('game', 'user', 'rating', 'created_at')
    list_filter = ('game', 'user')
    search_fields = ('game__title', 'user__username')


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('game', 'developer', 'submission_date', 'status')
    list_filter = ('developer', 'status', 'submission_date')
    search_fields = ('game__title', 'developer__username')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('game', 'caption')
    list_filter = ('game',)
    search_fields = ('game__title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name',)
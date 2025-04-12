from django.contrib import admin
from .models import UserProfile, Skill, Certification, Language, RatingSeller

class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1

class LanguageInline(admin.TabularInline):
    model = Language
    extra = 1

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'state', 'website_link', 'overall_rating')
    search_fields = ('user__username', 'country', 'state')
    list_filter = ('country', 'state')
    filter_horizontal = ('skills',)
    inlines = [CertificationInline, LanguageInline]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(RatingSeller)
class RatingSellerAdmin(admin.ModelAdmin):
    list_display = ('seller', 'reviewer', 'review_rating', 'created_at')
    search_fields = ('seller__user__username', 'reviewer__user__username', 'title')
    list_filter = ('created_at',)

# Optional: register Certification and Language if you want direct access from the admin menu
@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'title', 'issuing_organization', 'issue_date')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'language', 'proficiency')
    list_filter = ('proficiency',)

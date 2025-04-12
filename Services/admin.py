from django.contrib import admin
from .models import (
    Category,
    Overview,
    BasicPackage,
    StandardPackage,
    PremiumPackage,
    Description,
    Question,
    Gallery,
    RatingService
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class BasicPackageInline(admin.TabularInline):
    model = BasicPackage
    extra = 0

class StandardPackageInline(admin.TabularInline):
    model = StandardPackage
    extra = 0

class PremiumPackageInline(admin.TabularInline):
    model = PremiumPackage
    extra = 0

class DescriptionInline(admin.StackedInline):
    model = Description
    extra = 0

class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 0

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0

@admin.register(Overview)
class OverviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'titleOverview', 'category', 'overall_rating')
    search_fields = ('titleOverview', 'user__username', 'search_tags')
    list_filter = ('category',)
    inlines = [BasicPackageInline, StandardPackageInline, PremiumPackageInline, DescriptionInline, GalleryInline, QuestionInline]

@admin.register(RatingService)
class RatingServiceAdmin(admin.ModelAdmin):
    list_display = ('overview', 'reviewer', 'review_rating', 'title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('reviewer__user__username', 'overview__titleOverview', 'title')

# Optional: register separately if needed for standalone views
@admin.register(BasicPackage)
class BasicPackageAdmin(admin.ModelAdmin):
    list_display = ('overview', 'Basic_title', 'Basic_price', 'Basic_delivery_time', 'Basic_revisions', 'Basic_source_file')

@admin.register(StandardPackage)
class StandardPackageAdmin(admin.ModelAdmin):
    list_display = ('overview', 'Standard_title', 'Standard_price', 'Standard_delivery_time', 'Standard_revisions', 'Standard_source_file')

@admin.register(PremiumPackage)
class PremiumPackageAdmin(admin.ModelAdmin):
    list_display = ('overview', 'Premium_title', 'Premium_price', 'Premium_delivery_time', 'Premium_revisions', 'Premium_source_file')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('overview', 'question_text', 'question_type', 'allow_multiple_selection')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('overview', 'image1', 'image2', 'image3', 'video')

@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('overview', 'description')

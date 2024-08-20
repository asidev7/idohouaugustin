from django.contrib import admin
from .models import Contact, PricingPlan, Service, Skill, Project, Tag, BlogPost, SiteInformation, Testimonial
from main import models

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    search_fields = ('name',)
    list_filter = ('proficiency',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('skills_used',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'project_type','image', 'skills_used', 'url')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at', 'author')
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('tags',)
    readonly_fields = ('created_at', 'updated_at')


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'info', 'quote', 'profile_image')
    search_fields = ('name', 'info', 'quote')
    list_filter = ('info',)

    # Optional: Add image preview in the admin list view
    def profile_image_thumbnail(self, obj):
        if obj.profile_image:
            return '<img src="%s" width="50" height="50" />' % obj.profile_image.url
        else:
            return 'No image'
    profile_image_thumbnail.allow_tags = True
    profile_image_thumbnail.short_description = 'Profile Image'

    # Optionally, override form layout if needed
    fieldsets = (
        (None, {
            'fields': ('quote', 'name', 'info', 'profile_image')
        }),
    )
    
    

admin.site.register(Testimonial, TestimonialAdmin)


admin.site.register(Contact)
@admin.register(SiteInformation)
class SiteInformationAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'contact_email', 'poste','phone_number', 'created_at', 'updated_at')
    search_fields = ('site_name', 'contact_email', 'phone_number')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('site_name', 'poste','image', 'lien_youtube','contact_email', 'phone_number', 'postal_address')
        }),
        ('Payment Information', {
            'fields': ('paypal_link',),
            'classes': ('collapse',),
        }),
        ('Social Media', {
            'fields': ('facebook_link', 'twitter_link', 'linkedin_link', 'instagram_link'),
            'classes': ('collapse',),
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')
    search_fields = ('name', 'description')
    list_filter = ('price', 'duration')
    ordering = ('name',)
    readonly_fields = ('features',)  # Si vous voulez que le champ 'features' soit en lecture seule

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('plan_type', 'price', 'description')
    search_fields = ('description', 'features')
    list_filter = ('plan_type',)
    ordering = ('plan_type',)
    readonly_fields = ('features',)  
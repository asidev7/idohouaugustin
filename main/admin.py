from django.contrib import admin
from .models import Contact, Service, Skill, Project, Tag, BlogPost, SiteInformation

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
            'fields': ('title', 'slug', 'description', 'image', 'skills_used', 'url')
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


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title',)
    ordering = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'icon_class')
        }),
    )
    
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

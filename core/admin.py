from django.contrib import admin
from .models import ImageSetting, GeneralSetting, Skill, Experience, Education, SocialMedia, Document

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updated_date']
    search_fields = ['name', 'description', 'file']
    list_editable = ['description', 'file']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'icon')
    list_filter = ('name',)
    search_fields = ('name', 'description')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'job_title', 'job_location', 'end_date', 'start_date', 'updated_date']
    search_fields = ['company_name', 'job_title', 'job_location']
    list_editable = ['company_name', 'job_title', 'job_location', 'end_date', 'start_date']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_name', 'major', 'department', 'end_date', 'start_date', 'updated_date']
    search_fields = ['school_name', 'major', 'department']
    list_editable = ['school_name', 'major', 'department', 'end_date', 'start_date']

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'link', 'icon', 'updated_date']
    search_fields = ['link', 'icon']
    list_editable = ['order', 'link', 'icon']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'slug', 'button_text', 'file', 'updated_date']
    search_fields = ['slug', 'button_text']
    list_editable = ['order', 'slug', 'button_text', 'file']

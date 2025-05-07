from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia, Document
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''
    return obj

def get_image_setting(parameter):
    try:
        obj = ImageSetting.objects.get(name=parameter).file
    except:
        obj = ''
    return obj

def layout(request):
    site_title = get_general_setting('site_title')
    site_keywords = get_general_setting('site_keywords')
    site_description = get_general_setting('site_description')
    home_banner_name = get_general_setting('home_banner_name')
    home_banner_title = get_general_setting('home_banner_title')
    home_banner_description = get_general_setting('home_banner_description')
    about_myself_footer = get_general_setting('about_myself_footer')
    about_myself_welcome = get_general_setting('about_myself_welcome')

    home_banner_image = get_image_setting('home_banner_image')
    header_logo = get_image_setting('header_logo')
    site_favicon = get_image_setting('site_favicon')

    social_medias = SocialMedia.objects.all()
    documents = Document.objects.all()
    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_footer': about_myself_footer,
        'about_myself_welcome': about_myself_welcome,
        'header_logo': header_logo,
        'home_banner_image': home_banner_image,
        'site_favicon': site_favicon,
        'documents': documents,
        'social_medias': social_medias,
    }
    return context

def index(request):
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()

    context = {
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
    }
    return render(request, 'index.html', context=context)

def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.file.url)

class SkillListView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = 'index.html'
    context_object_name = 'skills'

class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    fields = ['order', 'name', 'description']
    template_name = 'service-details.html'
    success_url = reverse_lazy('skill_list')

class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = Skill
    fields = ['order', 'name', 'description']
    template_name = 'service-details.html'
    success_url = reverse_lazy('skill_list')

class SkillDeleteView(LoginRequiredMixin, DeleteView):
    model = Skill
    template_name = 'portfolio-details.html'
    success_url = reverse_lazy('skill_list')

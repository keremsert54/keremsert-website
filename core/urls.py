from django.urls import path
from .views import index, redirect_urls, SkillListView, SkillCreateView, SkillUpdateView, SkillDeleteView

urlpatterns = [
    path('', index, name='index'),
    path('<slug>/', redirect_urls, name='redirect_urls'),
    path('management/skills/', SkillListView.as_view(), name='skill_list'),
    path('management/skills/create/', SkillCreateView.as_view(), name='skill_create'),
    path('management/skills/<int:pk>/update/', SkillUpdateView.as_view(), name='skill_update'),
    path('management/skills/<int:pk>/delete/', SkillDeleteView.as_view(), name='skill_delete'),
]


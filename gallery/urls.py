from django.urls import path, re_path
from taggit.models import Tag

from . import views

app_name = "gallery"
urlpatterns = [
    path("", views.IndexView.as_view(extra_context={'tags': Tag.objects.all()}), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("", views.FilterIndexView.as_view(extra_context={'tags': Tag.objects.all()}), name="filter_index"),
    path('new/', views.post_new_func, name='post_new'),
    path('<int:pk>/edit/', views.post_edit_func, name='post_edit'),
    path('search_index', views.SearchIndexView.as_view(), name='search_index'),
    path('tag-autocomplete/', views.TagAutocomplete.as_view(), name='tag-autocomplete'),
    #path("", views.FilterIndexView.as_view(extra_context={'tags': Tag.objects.all()}), name="filter_index"),
]
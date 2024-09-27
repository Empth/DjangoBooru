from django.urls import path
from taggit.models import Tag

from . import views

app_name = "gallery"
urlpatterns = [
    path("", views.IndexView.as_view(extra_context={'tags': Tag.objects.all()}), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("q=<str:query>/", views.FilterIndexView.as_view(extra_context={'tags': Tag.objects.all()}), name="filter_index"),
    path('new/', views.post_new_func, name='post_new'),
    path('<int:pk>/edit/', views.post_edit_func, name='post_edit'),
]

#     path("q=<str:query>/", views.filterIndex, name="filter_index"), # TODO
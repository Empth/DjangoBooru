from django.urls import path, re_path
from taggit.models import Tag

from . import views

app_name = "gallery"
urlpatterns = [
    path("", views.IndexView.as_view(extra_context={'tags': Tag.objects.all()}), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('new/', views.post_new_func, name='post_new'),
    path('<int:pk>/edit/', views.post_edit_func, name='post_edit'),
    path('tag-autocomplete/', views.TagAutocomplete.as_view(), name='tag-autocomplete'),
    path('<post_id>/delete', views.delete_post, name='delete'),
    path('register', views.register_user, name='register_user'),
    path('login', views.login_user,  name='login_user')
]
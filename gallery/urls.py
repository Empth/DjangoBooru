from django.urls import path

from . import views

app_name = "gallery"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:image_id>/", views.detail, name="detail"),
    path("q=<str:query>/", views.filterIndex, name="filter_index"),
]
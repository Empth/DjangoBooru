from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ImagePost
from taggit.models import Tag

def index(request):
    latest_image_list = ImagePost.objects.order_by("-pub_date")[:10]
    tags = Tag.objects.all()
    context = {"latest_image_list": latest_image_list, 'tags': tags}
    return render(request, 'gallery/index.html', context)

def detail(request, image_id):
    image_post = get_object_or_404(ImagePost, pk=image_id)
    return render(request, "gallery/detail.html", {"image_post": image_post})
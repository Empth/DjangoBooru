from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ImagePost

def index(request):
    latest_image_list = ImagePost.objects.order_by("-pub_date")[:10]
    return render(request, 'gallery/index.html', {"latest_image_list": latest_image_list})

def detail(request, image_id):
    image_detail = get_object_or_404(ImagePost, pk=image_id)
    return render(request, "gallery/detail.html", {"image_detail": image_detail})
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from .models import ImagePost
from taggit.models import Tag
from django.db.models import F

class ExtraContext(object):
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(ExtraContext, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
    

class IndexView(generic.ListView, ExtraContext):
    template_name = "gallery/index.html"
    context_object_name = "latest_image_list"

    def get_queryset(self):
        """Return the last ten published image posts."""
        return ImagePost.objects.order_by("-pub_date")[:10]
    
    
class FilterIndexView(generic.ListView, ExtraContext):
    template_name = "gallery/filter_index.html"
    context_object_name = "latest_image_list"

    def get_queryset(self):
        # TODO Implement multi-tag filtering
        """Return the last ten published image posts, filtered with tag 'query'."""
        return ImagePost.objects.filter(tags__name__in=[self.kwargs['query']]).order_by("-pub_date")[:10]


class DetailView(generic.DetailView):
    model = ImagePost
    template_name = "gallery/detail.html"

'''
def index(request):
    latest_image_list = ImagePost.objects.order_by("-pub_date")[:10]
    tags = Tag.objects.all()
    context = {"latest_image_list": latest_image_list, 'tags': tags}
    return render(request, 'gallery/index.html', context)

def detail(request, image_id: int):
    image_post = get_object_or_404(ImagePost, pk=image_id)
    return render(request, "gallery/detail.html", {"image_post": image_post})

def filterIndex(request, query: str):
    # TODO Implement multi-tag filtering
    latest_image_list = ImagePost.objects.filter(tags__name__in=[query]).order_by("-pub_date")[:10]
    tags = Tag.objects.all()
    context = {"latest_image_list": latest_image_list, 'tags': tags}
    return render(request, 'gallery/filter_index.html', context)

'''
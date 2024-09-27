from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from .models import ImagePost
from taggit.models import Tag
from django.db.models import F
from .forms import PostForm
from django.utils import timezone

num_pages = 10

class ExtraContext(object):
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(ExtraContext, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
    

class IndexView(generic.ListView, ExtraContext):
    paginate_by = num_pages
    template_name = "gallery/index.html"
    context_object_name = "latest_image_list"

    def get_queryset(self):
        """Return the last ten published image posts."""
        return ImagePost.objects.order_by("-pub_date")
    
    
class FilterIndexView(generic.ListView, ExtraContext):
    paginate_by = num_pages
    template_name = "gallery/filter_index.html"
    context_object_name = "latest_image_list"

    def get_queryset(self):
        # TODO Implement multi-tag filtering
        """Return the last ten published image posts, filtered with tag 'query'."""
        return ImagePost.objects.filter(tags__name__in=[self.kwargs['query']]).order_by("-pub_date")


class DetailView(generic.DetailView):
    model = ImagePost
    template_name = "gallery/detail.html"


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post_tags = form.cleaned_data['tags']
            post.save()
            for tag in post_tags:
                post.tags.add(tag)

            # NOTE need to namespace ALL returns from now on
            return redirect('gallery:detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'gallery/post_edit.html', {'form': form})
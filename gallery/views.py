from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, QueryDict
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import ImagePost
from taggit.models import Tag
from django.db.models import F
from .forms import PostForm, PatForm
from django.utils import timezone
from taggit.managers import TaggableManager
from dal import autocomplete
from django.db.models.aggregates import Count

num_pages = 10

class ExtraContext(object):
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(ExtraContext, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
    

class SearchIndexView(generic.UpdateView):
    model = ImagePost
    form_class = PatForm
    template_name = 'gallery/search_index.html'

    def get_success_url(self):
        q = QueryDict(mutable=True)
        q.setlist('query', ['tag1', 'tag2'])
        query_string = q.urlencode()
        base_url = reverse_lazy('gallery:index')
        return f"{base_url}?{query_string}"

    def get_object(self):
        return Tag.objects.first()
    

class IndexView(generic.ListView, ExtraContext):
    paginate_by = num_pages
    template_name = "gallery/index.html"
    context_object_name = "latest_image_list"

    def get_queryset(self):
        """Return the last ten published image posts."""
        queries = self.request.GET.getlist('query')
        displayed_images = ImagePost.objects.all()
        for query in queries:
            displayed_images = displayed_images.filter(tags__name__in=[query])
        return displayed_images.order_by("-modified_date")
    


class FilterIndexView(generic.ListView, ExtraContext):
    paginate_by = num_pages
    template_name = "gallery/filter_index.html"
    context_object_name = "latest_image_list"

    def get_queryset(self):
        # TODO Implement multi-tag filtering
        """Return the last ten published image posts, filtered with tag 'query'."""

        tags = self.kwargs['query']
        return ImagePost.objects.filter(tags__name__in=[self.kwargs['query']]).order_by("-modified_date")


class DetailView(generic.DetailView):
    model = ImagePost
    template_name = "gallery/detail.html"


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        '''
        if not self.request.user.is_authenticated():
            return Tag.objects.none() # ??
        '''

        qs = Tag.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
            #qs = qs.annotate(num_times=Count('taggit_taggeditem_items')).order_by("-num_times")
        return qs


# Note, there is a bug with this function where if a new tag is uploaded alongside an image, then
# the new tag doesn't show up in the gallery page.
# NOTE, NOT a browser cache issue
# NOTE, it's an issue with the admin post; not really a prob from the form
def post_new_func(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            post.update_tags(form.cleaned_data['tags'])
            # NOTE need to namespace ALL returns from now on
            return redirect('gallery:detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'gallery/post_edit.html', {'form': form})


# Note, the post edit function has the same tag bug as post_new_func 
def post_edit_func(request, pk):
    post = get_object_or_404(ImagePost, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.modified_date = timezone.now()
            post.save()
            post.update_tags(form.cleaned_data['tags'])
            return redirect('gallery:detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'gallery/post_edit.html', {'form': form})

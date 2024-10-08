from django import forms

from .models import ImagePost
from dal import autocomplete
from taggit.models import Tag

class PostForm(forms.ModelForm):
    # Note for image upload forms, the template form needs enctype="multipart/form-data"
    # and the respective view's FileUploadForm needs the request.FILES field, otherwise file/image
    # upload does not work.
    class Meta:
        model = ImagePost
        fields = ['image', 'description', 'tags']


# Pat == ImagePost
class PatForm(autocomplete.FutureModelForm):
    class Meta:
        model = ImagePost
        fields = ('tags',) # ??
        widgets = {
            'tags': autocomplete.TagSelect2(url='gallery:tag-autocomplete'), 
        }
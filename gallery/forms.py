from django import forms

from .models import ImagePost

class PostForm(forms.ModelForm):
    # Note for image upload forms, the template form needs enctype="multipart/form-data"
    # and the respective view's FileUploadForm needs the request.FILES field, otherwise file/image
    # upload does not work.
    class Meta:
        model = ImagePost
        fields = ['image', 'description', 'tags']